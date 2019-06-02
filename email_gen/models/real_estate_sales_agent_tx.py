import collections
from django.db import models
from .licensee import Licensee
from ..constants import TREC_LIC_STATUS, TREC_LIC_TYPES, TREC_ED_STATUS, TREC_MCE_STATUS
from .transforms import name_transform, date_transformer, county_code_transform
from ..utils import compose


class RealEstateSalesAgentTexas(Licensee):
    trec_county = models.IntegerField(blank=True, null=True)

    # License Fields
    lic_number = models.CharField(blank=True, max_length=20)  # Not guaranteed to be unique across all lists
    lic_status = models.CharField(blank=True, null=True, choices=TREC_LIC_STATUS, max_length=255)
    lic_type = models.CharField(blank=True, null=True, choices=TREC_LIC_TYPES, max_length=255)
    lic_date_orig = models.DateField(blank=True, null=True)
    lic_date_exp = models.DateField(blank=True, null=True)

    # Education Fields
    trec_ed_status = models.CharField(blank=True, null=True, choices=TREC_ED_STATUS, max_length=255)
    trec_mce_status = models.CharField(blank=True, null=True, choices=TREC_MCE_STATUS, max_length=255)
    designated_supervisor = models.CharField(blank=True, null=True, max_length=1)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Get the field labels to cache them and return
        # a function that will use them
        field_labels = source_instance.get_meta()
        # Compose the transforms for this model into a pipeline
        pipeline = compose(
            name_transform,
            date_transformer('lic_date_orig'),
            date_transformer('lic_date_exp'),
            county_code_transform
        )

        # Curried closure that makes the licensee using field_labels variable
        def make_licensee(licensee: collections.namedtuple):
            # Convert licensee from named tuple to dict with list fields
            licensee = dict(zip(field_labels, licensee))
            licensee = pipeline(licensee)

            # Add source
            licensee['source_list'] = source_instance
            # Spread the dictionary into kwargs
            return cls(**licensee)

        return make_licensee
