from .models import AppraiserTexas, InspectorTexas, RealEstateSalesAgentTexas, RealEstateSalesAgentApplicantTexas
from .list_filter import FilterFormTREC, FilterFormAPTX, FilterFormINTX, FilterFormREIApp


def get_resources_for(file_id):
    # Convenience dictionary for accessing
    # email list resources
    LIST_RESOURCES = {
        'trec': {
            'model': RealEstateSalesAgentTexas,
            'template': 'list-filter-trec',
            'filter_form': FilterFormTREC
        },
        'aptx': {
            'model': AppraiserTexas,
            'template': 'list-filter-aptx',
            'filter_form': FilterFormAPTX
        },
        'intx': {
            'model': InspectorTexas,
            'template': 'list-filter-intx',
            'filter_form': FilterFormINTX
        },
        'retx-prep': {
            'model': RealEstateSalesAgentApplicantTexas,
            'template': 'list-filter-retx-prep',
            'filter_form': FilterFormREIApp
        }
    }

    return LIST_RESOURCES[file_id]
