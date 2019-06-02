import collections
from django.db import models
from .licensee import Licensee
from ..constants import TREC_LIC_TYPES
from .transforms import name_transform, date_transformer
from ..utils import compose


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
        pipeline = compose(
            name_transform,
            date_transformer('app_date_orig'),
            date_transformer('app_date_exp')
        )

        def make_licensee(licensee: collections.namedtuple):
            # Don't need first value
            licensee = licensee[1:]
            licensee = pipeline(licensee)

            # Add source
            licensee['source_list'] = source_instance

            # Spread the dictionary into kwargs
            return cls(**licensee)

        return make_licensee
