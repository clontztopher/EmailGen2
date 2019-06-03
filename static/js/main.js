// Save List Buttons
$saveBtns = $('.save-list');
if ($saveBtns.length) {
    $saveBtns.on('click', function () {
        let $this = $(this);
        let listId = $this.attr('id');
        $this.attr('disabled', true)
            .removeClass('btn-primary')
            .addClass('btn-secondary')
            .find('i')
            .addClass('fa-spin');
        // $this.find('i').addClass('fa-spin');
        $.get('/fetch-save/' + listId + '/')
            .then(function (data) {
                $this.closest('.row').find('.updated').text(data.updated);
            })
            .always(function () {
                $this.attr('disabled', false)
                    .removeClass('btn-secondary')
                    .addClass('btn-primary')
                    .find('i')
                    .removeClass('fa-spin');
            })
    });
}

