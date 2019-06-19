from django.db import models
from .licensee import Licensee
from . import transforms
from ..utils import compose


class RealEstateSalesAgentOklahoma(Licensee):
    # License Fields
    lic_number = models.CharField(blank=True, max_length=20)  # Not guaranteed to be unique across all lists
    lic_status = models.CharField(blank=True, null=True, choices=(("A", "Active"), ("I", "Inactive")), max_length=1)
    lic_type = models.CharField(blank=True, null=True, choices=(('BR', 'Broker'), ('SA', 'Sales Agent')), max_length=2)
    lic_date_exp = models.DateField(blank=True, null=True)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Compose transformations
        return compose(
            lambda licensee: cls(**licensee),
            transforms.source_adder(source_instance),
            transforms.name_transform,
            transforms.date_transformer('lic_date_exp'),
            transforms.make_field_stripper(cls),
            transforms.licensee_zipper(source_instance.get_meta())
        )
