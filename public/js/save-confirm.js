jQuery(function ($) {
    let $saveForm = $('#save-list');
    let $submitBtn = $('input[type=submit]');
    let $progress = $('.progress');
    $saveForm.on('submit', function (e) {
        $submitBtn.attr('disabled', true);
        $progress.removeClass('d-none');
        console.log('submitted form');
        e.preventDefault();
        formData = $(this).serializeArray();
        $.post('/list-save/', formData)
            .then(function (data) {
                console.log(data)
                $submitBtn.attr('disabled', false);
                $progress.addClass('d-none');
            })
    });
    let $selects = $('select');
    $selects.on('change', function (e) {
        let $input = $(this).closest('.col').find('input');
        if (!$input.val()) {
            $input.val(e.target.value)
        }
    });
});