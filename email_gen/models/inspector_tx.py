from django.db import models
from .licensee import Licensee
from ..constants import TREC_LIC_STATUS, TREC_LIC_TYPES, TREC_ED_STATUS, TREC_MCE_STATUS
from ..utils import compose
from . import transforms


class InspectorTexas(Licensee):
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
        # Compose transformations
        return compose(
            lambda licensee: cls(**licensee),
            transforms.source_adder(source_instance),
            transforms.name_transform,
            transforms.date_transformer('lic_date_exp'),
            transforms.date_transformer('lic_date_orig'),
            transforms.county_code_transform,
            transforms.make_field_stripper(cls),
            transforms.licensee_zipper(source_instance.get_meta())
        )
