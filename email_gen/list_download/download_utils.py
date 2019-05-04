from .download_form_aptx import ApTxFilterForm
from .download_form_retx import TrecFilterForm
from .download_form_retxprep import RealEstatePrepTexasForm


def get_form_for(list_type):
    if list_type == 'aptx':
        return ApTxFilterForm
    if list_type == 'retx':
        return TrecFilterForm
    if list_type == 'retxprep':
        return RealEstatePrepTexasForm
