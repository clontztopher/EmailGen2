import pandas as pd
from nameparser import HumanName
from django.db.models import Model
from typing import Type


def licensee_zipper(field_labels: list):
    def zip_licensee(licensee_data: list):
        return dict(zip(field_labels, licensee_data))

    return zip_licensee


def make_field_stripper(model: Type[Model]):
    def strip_extra(licensee: dict):
        return {
            k: v for k, v in licensee.items() if k in [
                f.name for f in model._meta.get_fields()
            ]
        }

    return strip_extra


def source_adder(source_instance: Type[Model]):
    def add_source(licensee: dict):
        licensee['source_list'] = source_instance
        return licensee

    return add_source


def name_transform(licensee: dict):
    if licensee.setdefault('fullname', '') != '':
        fullname = HumanName(licensee['fullname'])
        fullname.capitalize()
        licensee['fullname'] = str.title(getattr(fullname, 'full_name'))
        licensee['firstname'] = getattr(fullname, 'first', '')
        licensee['middlename'] = getattr(fullname, 'middle', '')
        licensee['lastname'] = getattr(fullname, 'last', '')
    else:
        licensee['firstname'] = str.title(licensee['firstname'])
        licensee['middlename'] = str.title(licensee['firstname'])
        licensee['lastname'] = str.title(licensee['lastname'])
    return licensee


def date_transformer(field_name: str):
    def transform_date(licensee: dict):
        # Convert date strings to dates and check if they are null.
        # If null, supply None as field value so it can be entered
        # in database as such since the database library doesn't
        # recognize Pandas NaTType
        date = pd.to_datetime(licensee[field_name])
        if pd.isnull(date):
            date = None
        licensee[field_name] = date
        return licensee

    return transform_date


def county_code_transform(licensee: dict):
    # Change county code to int
    try:
        licensee['trec_county'] = int(licensee['trec_county'])
    except:
        licensee['trec_county'] = 0
    return licensee
