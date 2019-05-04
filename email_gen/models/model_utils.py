from django.db.models import Model

from .models_retx import RealEstateTexasListModel, RealEstateAgentTexasModel
from .models_aptx import AppraiserTexasListModel, AppraiserTexasModel
from .models_retxprep import RealEstateTexasPrepListModel, RealEstateTexasPrepModel


def get_models(list_type) -> (Model, Model):
    if list_type == 'aptx':
        return AppraiserTexasListModel, AppraiserTexasModel
    if list_type == 'retx':
        return RealEstateTexasListModel, RealEstateAgentTexasModel
    if list_type == 'retxprep':
        return RealEstateTexasPrepListModel, RealEstateTexasPrepModel
