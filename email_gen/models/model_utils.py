from django.db.models import Model
from . import models_aptx as aptx, models_retx as retx


def get_models(list_type) -> (Model, Model):
    if list_type == 'aptx':
        return aptx.AppraiserTexasListModel, aptx.AppraiserTexasModel
    if list_type == 'retx':
        return retx.RealEstateTexasListModel, retx.RealEstateAgentTexasModel
