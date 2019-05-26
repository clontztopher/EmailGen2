from .source_list import SourceListModel
from .appraiser_tx import AppraiserTexas
from .inspector_tx import InspectorTexas
from .real_estate_sales_agent_tx import RealEstateSalesAgentTexas
from .re_license_applicant_tx import RealEstateSalesAgentApplicantTexas


def temp_get_from_id(file_id):
    if file_id == 'intx':
        return InspectorTexas
    if file_id == 'aptx':
        return AppraiserTexas
    if file_id == 'trec':
        return RealEstateSalesAgentTexas
    if file_id == 'retx-prep':
        return RealEstateSalesAgentApplicantTexas
