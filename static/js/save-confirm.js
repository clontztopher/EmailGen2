jQuery(function ($) {
    let $saveForm = $('#save-list');
    let $submitBtn = $('input[type=submit]');
    let $progress = $('.progress');
    let $saveStatus = $('#save-status');
    $saveForm.on('submit', function (e) {
        $submitBtn.attr('disabled', true);
        $progress.removeClass('d-none');
        $saveStatus.addClass('d-none');
        e.preventDefault();
        formData = $(this).serializeArray();
        $.post('/list-save/', formData)
            .then(function (data) {
                if (data.status == 200) {
                    window.location = '/download-form/' + formData.find(x => x.name == 'file_name').value + '/';
                } else {
                    $saveStatus.removeClass('d-none')
                }
            })
            .always(function () {
                $submitBtn.attr('disabled', false);
                $progress.addClass('d-none');
            });
    });
    let $selects = $('select');
    $selects.on('change', function (e) {
        let $input = $(this).closest('.col').find('input');
        if (!$input.val()) {
            $input.val(e.target.value)
        }
    });
});