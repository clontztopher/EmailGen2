import pandas as pd

from ..models.model_utils import get_models


def save_list(list_type, file):
    list_model, entity_model = get_models(list_type)
    try:
        list_instance = list_model.objects.get(list_type=list_type)
    except:
        list_instance = list_model()

    list_instance.save()

    # "Truncate" table before entering new from list
    entity_model.objects.all().delete()

    opts = list_model.get_reader_opts()
    reader = pd.read_csv(file, **opts)

    for chunk in reader:
        chunk.fillna('')
        entities = []

        for entity in chunk.itertuples():
            entity_attrs = entity._asdict()
            del entity_attrs['Index']
            entity_attrs['source_list'] = list_instance
            entities.append(entity_model(**entity_attrs))

        entity_model.objects.bulk_create(entities)

    return list_instance
