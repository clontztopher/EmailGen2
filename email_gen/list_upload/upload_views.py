import random
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .upload_form import SourceListUploadForm

from ..models import SourceListModel, Person, TextAttribute, DateAttribute, NumericAttribute, EmailAttribute
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
    list_fields, list_types = source_instance.get_meta()
    if not list_fields:
        list_fields = ['' for _ in range(len(sample))]
        list_types = list_fields
    list_data = list(zip(list_fields, list_types, sample))
    return render(request, 'email_gen/list-config.html',
                  {'source': source_instance, 'list_data': list_data})


def list_save(request):
    if request.method == 'POST':
        # Data prep
        file_name = request.POST['file_name']
        field_labels = request.POST.getlist('field_label')
        field_labels = [l if (l != '') else ('field_' + str(i)) for i, l in enumerate(field_labels)]
        field_types = request.POST.getlist('field_type')
        person_field_type_names = ('fullname', 'firstname', 'middlename', 'lastname', 'suffix')

        # File fetch
        reader = get_file_reader(file_name, chunksize=5000)

        # Database Stuff
        source_instance = SourceListModel.objects.get(file_name=file_name)
        source_instance.field_labels = str.join('::', field_labels)
        source_instance.field_types = str.join('::', field_types)
        source_instance.save()

        # Clear out list
        if hasattr(source_instance, 'people'):
            source_instance.people.all().delete()

        for chunk in reader:
            chunk = chunk.fillna('')

            people = []
            email_attrs = []
            text_attrs = []
            date_attrs = []
            numeric_attrs = []

            for person_data in chunk.itertuples(name=None, index=False):

                person = Person(source_list=source_instance, id=random.getrandbits(32))
                people.append(person)

                for j, (field_type, field_label) in enumerate(zip(field_types, field_labels)):

                    attr_val = person_data[j]

                    if field_type in person_field_type_names:
                        setattr(person, field_type, attr_val)
                        continue

                    if field_type == 'email':
                        email_attrs.append(
                            EmailAttribute(email=attr_val, person=person, field_label=field_label)
                        )
                        continue

                    if field_type == 'text':
                        text_attrs.append(
                            TextAttribute(text=attr_val, person=person, field_label=field_label)
                        )
                        continue

                    if field_type == 'date':
                        date = pd.to_datetime(attr_val)
                        date_attrs.append(
                            DateAttribute(date=date, person=person, field_label=field_label)
                        )
                        continue

                    if field_type == 'numeric':
                        numeric_attrs.append(
                            NumericAttribute(num=attr_val, person=person, field_label=field_label)
                        )
                        continue

            Person.objects.bulk_create(people)
            EmailAttribute.objects.bulk_create(email_attrs)
            TextAttribute.objects.bulk_create(text_attrs)
            DateAttribute.objects.bulk_create(date_attrs)
            NumericAttribute.objects.bulk_create(numeric_attrs)

            print('chunk added')

        print('Data save complete')

    return JsonResponse({})
