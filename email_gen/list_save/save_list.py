from ..file_storage.file_storage import FileStorageService
from ..models import SourceListModel, temp_get_from_id


def save_list(file_id):
    """
    Saves list from bucket to database
    :param file_id:
    :return: None
    """
    source_instance = SourceListModel.objects.get(file_id=file_id)
    storage_service = FileStorageService()
    reader = storage_service.get_file_reader(file_id, chunksize=5000)

    # Feels dirty, need to fix somehow
    licensee_class = temp_get_from_id(file_id)
    licensee_class.objects.all().delete()
    make_licensee = licensee_class.licensee_maker(source_instance)

    # Loop over dataframe that is a chunk of lines in the file
    # and create a 'people' list to bulk create instances
    for chunk in reader:
        chunk = chunk.fillna('')
        licensees = []

        # Loop over the lines in the file data chunk
        # creating a Person instance from each
        for licensee_data in chunk.itertuples(index=False, name='Licensee'):
            licensee = make_licensee(licensee_data, source_instance)
            if licensee:
                licensees.append(licensee)

        licensee_class.objects.bulk_create(licensees)

    # Return source update date in case
    # caller wants to display it somewhere
    return source_instance.update_date
