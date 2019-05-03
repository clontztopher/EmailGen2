from .download_form_aptx import ApTxFilterForm
from .download_form_retx import TrecFilterForm


def get_form_for(list_type):
    if list_type == 'aptx':
        return ApTxFilterForm
    if list_type == 'retx':
        return TrecFilterForm
