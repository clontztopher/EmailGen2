import collections
from django.db import models
import pandas as pd
from .licensee import Licensee
from ..constants import TREC_LIC_TYPES


class RealEstateSalesAgentApplicantTexas(Licensee):
    # License Fields
    lic_type = models.CharField(blank=True, null=True, choices=TREC_LIC_TYPES, max_length=255)
    app_date_orig = models.DateField(blank=True, null=True)
    app_date_exp = models.DateField(blank=True, null=True)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Get the field labels to cache them and return
        # a function that will use them
        field_labels = source_instance.get_meta()

        def make_licensee(licensee: collections.namedtuple, source_instance):
            # Don't need first value
            licensee = licensee[1:]
            # Convert licensee from named tuple to dict with list fields
            licensee = dict(zip(field_labels, licensee))
            # Convert date strings to dates and check if they are null.
            # If null, supply None as field value so it can be entered
            # in database as such since the database library doesn't
            # recognize Pandas NaTType
            date_orig = pd.to_datetime(licensee['app_date_orig'])
            if pd.isnull(date_orig):
                date_orig = None
            licensee['app_date_orig'] = date_orig

            date_exp = pd.to_datetime(licensee['app_date_exp'])
            if pd.isnull(date_exp):
                date_exp = None
            licensee['app_date_exp'] = date_exp
            # Add source
            licensee['source_list'] = source_instance

            # Spread the dictionary into kwargs
            return cls(**licensee)

        return make_licensee
