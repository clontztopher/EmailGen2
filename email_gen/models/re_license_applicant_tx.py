from django.db import models
from .licensee import Licensee
from ..constants import TREC_LIC_TYPES
from . import transforms
from ..utils import compose


class RealEstateSalesAgentApplicantTexas(Licensee):
    # License Fields
    lic_type = models.CharField(blank=True, null=True, choices=TREC_LIC_TYPES, max_length=255)
    app_date_orig = models.DateField(blank=True, null=True)
    app_date_exp = models.DateField(blank=True, null=True)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Compose transformations
        return compose(
            lambda licensee: cls(**licensee),
            transforms.source_adder(source_instance),
            transforms.name_transform,
            transforms.date_transformer('app_date_orig'),
            transforms.date_transformer('app_date_exp'),
            transforms.make_field_stripper(cls),
            transforms.licensee_zipper(source_instance.get_meta()),
            # Drop applicant ID, not needed
            lambda licensee: licensee[1:]
        )
