import collections
from django.db import models
from .licensee import Licensee
from ..constants import TREC_LIC_STATUS, TALCB_LIC_TYPES
from ..utils import compose
from .transforms import name_transform, date_transformer, county_code_transform


class AppraiserTexas(Licensee):
    lic_number = models.CharField(blank=True, max_length=20)  # Not guaranteed to be unique across all lists
    lic_status = models.CharField(blank=True, null=True, choices=TREC_LIC_STATUS, max_length=255)
    lic_type = models.CharField(blank=True, null=True, choices=TALCB_LIC_TYPES, max_length=255)
    lic_date_orig = models.DateField(blank=True, null=True)
    lic_date_exp = models.DateField(blank=True, null=True)
    trec_county = models.IntegerField(blank=True, null=True)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Get the field labels to cache them and return
        # a function that will use them
        field_labels = source_instance.get_meta()
        # Compose the transforms for this model into a pipeline
        pipeline = compose(
            name_transform,
            date_transformer('lic_date_exp'),
            date_transformer('lic_date_orig'),
            county_code_transform
        )

        def make_licensee(licensee: collections.namedtuple):
            # Convert licensee from named tuple to dict with list fields
            licensee = dict(zip(field_labels, licensee))
            licensee = pipeline(licensee)

            # Add source
            licensee['source_list'] = source_instance
            # Spread the dictionary into kwargs
            return cls(**licensee)

        return make_licensee
