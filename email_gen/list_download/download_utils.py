import pandas as pd

from ..models.model_utils import get_models
from . import download_form_aptx as aptx_form, download_form_retx as retx_form


def download_list(list_type, query_set, file_obj):
    list_model, list_entity = get_models(list_type)
    df = pd.DataFrame(list(query_set.values()), columns=list_model.FILE_HEADERS)
    df.to_csv(path_or_buf=file_obj, mode='a')
    return file_obj


def get_form_for(list_type):
    if list_type == 'aptx':
        return aptx_form
    if list_type == 'retx':
        return retx_form
