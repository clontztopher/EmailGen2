// General form handler to stop propagation, call the passed-in handler
// and disable submit button. Also re-enables the submit button once
// ajax request has completed
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
            console.log(data)
        }).fail(function (err) {
            console.warn(err)
        })
    });
}




