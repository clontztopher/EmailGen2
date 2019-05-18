import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .upload_form import SourceListUploadForm

from ..models import SourceListModel, Person
from .person_builder import build_person
from ..file_storage.file_storage import get_list_sample, get_source_bucket, get_file_reader


def upload_list(request, file_name=None):
    available_lists = SourceListModel.objects.all()
    display_name = None
    if file_name:
        display_name = available_lists.get(file_name=file_name).display_name
    if request.method == 'POST':
        form = SourceListUploadForm(request.POST, request.FILES)

        if form.is_valid():
            display_name = form.cleaned_data['list_name']
            file_ext = os.path.splitext(request.FILES['file'].name)[-1]
            file_name = display_name.replace(' ', '-') + file_ext

            try:
                SourceListModel.objects.get(file_name=file_name)
            except:
                SourceListModel.objects.create(file_name=file_name, display_name=display_name)

            bucket = get_source_bucket()
            blob = bucket.blob(file_name)
            blob.upload_from_file(request.FILES['file'])

            return redirect('/list-config/%s/' % file_name)

    form = SourceListUploadForm(initial={'list_name': display_name})
    return render(request, 'email_gen/upload-form.html', {
        'form': form,
        'available_lists': available_lists
    })


def list_config(request, file_name):
    sample = get_list_sample(file_name)
    source_instance = SourceListModel.objects.get(file_name=file_name)
    field_opts = [f.name for f in Person._meta.get_fields() if f.name not in ('source_list', 'uuid')]

    # Prepend 'None' to be the default option
    field_opts = ['None'] + field_opts

    # Get existing list fields or a list of 'None'
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

        # Get the source list instance and field label metadata
        source_instance = SourceListModel.objects.get(file_name=file_name)
        source_instance.field_labels = str.join('::', field_labels)
        source_instance.save()

        if request.POST['headers-only'] == '1':
            return JsonResponse({'status': 200})

        # File fetch
        reader = get_file_reader(file_name, chunksize=5000)

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
                person = build_person(source_instance, person_data, field_labels)
                people.append(person)

            Person.objects.bulk_create(people)

            print('chunk added')
        print('Data save complete')

    return JsonResponse({
        'status': 200
    })
