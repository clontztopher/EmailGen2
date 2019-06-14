import collections
from django.db import models
from .licensee import Licensee
from .transforms import name_transform, date_transformer
from ..utils import compose


class RealEstateSalesAgentTexas(Licensee):
    # License Fields
    lic_number = models.CharField(blank=True, max_length=20)  # Not guaranteed to be unique across all lists
    lic_status = models.CharField(blank=True, null=True, choices=(("A", "Active"), ("I", "Inactive")), max_length=1)
    lic_type = models.CharField(blank=True, null=True, choices=(('BR', 'Broker'), ('SA', 'Sales Agent')), max_length=2)
    lic_date_exp = models.DateField(blank=True, null=True)

    @classmethod
    def licensee_maker(cls, source_instance):
        # Get the field labels to cache them and return
        # a function that will use them
        field_labels = source_instance.get_meta()
        # Compose the transforms for this model into a pipeline
        pipeline = compose(
            name_transform,
            date_transformer('lic_date_exp'),
        )

        # Curried closure that makes the licensee using field_labels variable
        def make_licensee(licensee: collections.namedtuple):
            # Convert licensee from named tuple to dict with list fields
            # zip only matches up to the end of the shortest list so extraneous
            # fields at the end may be left off
            licensee = dict(zip(field_labels, licensee))

            # Run licensee through the transformation pipeline
            licensee = pipeline(licensee)

            # Add source related field to licensee
            licensee['source_list'] = source_instance

            # Spread the dictionary into kwargs
            return cls(**licensee)

        return make_licensee
