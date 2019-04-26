from .download import aptx, trec


def get_form_for(type):
    return {
        'aptx': aptx.ApTxFilterForm,
        'retx': trec.TrecFilterForm
    }[type]
