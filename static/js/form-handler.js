function setFormHandler(formHandler) {
    let $form = $('form');
    let $submitBtn = $('button[type=submit]');

    $form.on('submit', function (e) {
        $submitBtn.attr('disabled', true);
        $submitBtn.find('i').addClass('fa-spin');

        e.preventDefault();

        // Use instance of FormData to provide file in post request
        let formData = new FormData(this);

        formHandler(formData)
            .always(function () {
                $submitBtn.attr('disabled', false);
                $submitBtn.find('i').removeClass('fa-spin');
            });
    });
}

if ($('form#save-list').length) {
    setFormHandler(function (formData) {
        return $.ajax({
            url: '/list-save/',
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false
        }).then(function (data) {
            if (data.status == 200) {
                window.location = '/download-form/' + data.fileName + '/';
            }
        })
    });
}

if ($('form#upload-form').length) {

    // Set the form handler
    setFormHandler(function (formData) {
        return $.ajax({
            url: '/upload/',
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false
        }).then(function (data) {
            if (data.status == 200) {
                window.location = '/list-config/' + data.fileName + '/';
            }
        })
    });

    // Set select to 'None' when adding a new list in case a list
    // was already selected previously
    let $listSelect = $('#id_existing_lists');
    $('#id_new_list').on('keydown', function (e) {
        $listSelect.find('option:eq(0)').prop('selected', true);
    });
}
