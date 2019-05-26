import pandas as pd
from nameparser import HumanName
from ..constants import TREC_LIC_STATUS


def make_licensee(source_instance, person_data, field_labels):
    person = Person(source_list=source_instance)
    # Loop over the line/person data and add values to the
    # Person instance for database insertion
    for j, field_label in enumerate(field_labels):

        # Skip untagged fields
        if field_label == 'None':
            continue

        # Split a fullname out into first, middle and last
        if field_label == 'fullname':
            name = HumanName(val)
            name.capitalize()
            person.firstname = getattr(name, 'first', '')
            person.middlename = getattr(name, 'middle', '')
            person.lastname = getattr(name, 'last', '')
            continue

        # Get field data
        val = person_data[j]

        # Format names to title case
        if field_label in ('firstname', 'middlename', 'lastname'):
            val = val.title()

        # Strip spaces if string
        if type(val) == str:
            val = val.strip()

        # Oklahoma license type conversion
        if field_label == 'lic_type':
            if val == 'I':
                val = 'INA'
            if val == 'A':
                val = 'ACT'

        # Make sure empty dates are saved as
        # None instead of Pandas NaT type
        if 'date' in field_label:
            if val != '':
                val = pd.to_datetime(val)
            else:
                val = None

        # Set attribute on person to save
        setattr(person, field_label, val)

    return person
