import random
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .upload_form import SourceListUploadForm

from ..models import SourceListModel, Person
from ..file_storage.file_storage import get_list_sample, get_source_bucket, get_file_reader


def upload_list(request):
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file_name = request.FILES['file'].name
            display_name = form.cleaned_data['list_name']
            try:
                SourceListModel.objects.get(file_name=file_name)
            except:
                SourceListModel.objects.create(file_name=file_name, display_name=display_name)

            bucket = get_source_bucket()
            blob = bucket.blob(file_name)
            blob.upload_from_file(request.FILES['file'])

            return redirect('/list-config/%s/' % file_name)

    form = SourceListUploadForm()
    return render(request, 'email_gen/upload-form.html', {'form': form})


def list_config(request, file_name):
    sample = get_list_sample(file_name)
    source_instance = SourceListModel.objects.get(file_name=file_name)
    field_opts = [f.name for f in Person._meta.get_fields() if f.name not in ('source_list', 'id')]

    # Prepend 'None' to be the default option
    field_opts = ['None'] + field_opts

    # Get existing list fields or a list of empty strings
    list_fields = source_instance.get_meta()
    if not list_fields:
        list_fields = ['None' for _ in range(len(sample))]

    list_data = list(zip(list_fields, sample))

    return render(request, 'email_gen/list-config.html', {
        'source': source_instance,
        'field_opts': field_opts,
        'list_data': list_data
    })


def list_save(request):
    if request.method == 'POST':
        # Data prep
        file_name = request.POST['file_name']
        field_labels = request.POST.getlist('field_labels')

        # File fetch
        reader = get_file_reader(file_name, chunksize=5000)

        # Get the source list instance and field label metadata
        source_instance = SourceListModel.objects.get(file_name=file_name)
        source_instance.field_labels = str.join('::', field_labels)
        source_instance.save()

        # Clear out current db data for list
        if hasattr(source_instance, 'people'):
            source_instance.people.all().delete()

        # Loop over dataframe that is a chunk of lines in the file
        # and create a 'people' list to bulk create instances
        for chunk in reader:
            chunk = chunk.fillna('')
            people = []

            # Loop over the lines in the file data chunk
            # creating a Person instance from each
            for person_data in chunk.itertuples(name=None, index=False):
                person = Person(source_list=source_instance, id=random.getrandbits(32))
                people.append(person)

                # Loop over the line/person data and add values to the
                # Person instance for database insertion
                for j, field_label in enumerate(field_labels):
                    val = person_data[j]

                    if field_label == 'lic_type' and val == 'I':
                        val = 'INA'
                    if field_label == 'lic_type' and val == 'A':
                        val = 'ACT'
                    if type(val) == str:
                        val = val.strip()
                    if 'date' in field_label:
                        val = pd.to_datetime(val)
                    setattr(person, field_label, val)

            Person.objects.bulk_create(people)

            print('chunk added')

        print('Data save complete')

    return JsonResponse({})
