from email_gen import models, sources_conf


def save_source(file_id, reader):
    """
    Saves list from reader to database
    """
    source_instance = models.SourceListModel.objects.get(file_id=file_id)
    licensee_class = getattr(models, sources_conf.SOURCE_CONFIG[file_id]['model'])

    # Delete licensees for current list and start fresh
    licensee_class.objects.all().delete()
    # Create a licensee-maker function
    make_licensee = licensee_class.licensee_maker(source_instance)

    # Loop over dataframe that is a chunk of lines in the file
    # and create a 'people' list to bulk create instances
    for chunk in reader:
        # Can't save Pandas NaT Type so convert to empty string
        chunk = chunk.fillna('')
        # Container for model objects
        licensees = []

        # Loop over the lines in the file data chunk
        # creating a Person instance from each
        for licensee_data in chunk.itertuples(index=False, name='Licensee'):
            licensee = make_licensee(licensee_data)
            if licensee:
                licensees.append(licensee)

        # Bulk create the list of new licensee objects
        licensee_class.objects.bulk_create(licensees)
        print('Chunk added, count: ' + str(len(licensees)))

    # Return source update date in case
    # it needs to be displayed it somewhere
    source_instance.save()
    return source_instance.update_date
