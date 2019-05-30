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


// jQuery(function ($) {
//     // Initialize flatpickr for page inputs
//     flatpickr('.flatpickr');
//
//     $('.date-inputs').each(function () {
//         let $fieldContainer = $(this);
//         let $individualDateContainer = $fieldContainer.find('#individual-date-container .card-body');
//         let $addDateBtn = $individualDateContainer.find('button');
//         let $baseClone = $individualDateContainer.find('.form-group.row').clone();
//
//         $baseClone
//             .find('input')
//             .attr('id', removeIndex)
//             .attr('name', removeIndex)
//             .val('');
//
//         $addDateBtn.on('click', function (e) {
//             e.preventDefault();
//             let $indieDateRows = $individualDateContainer.find('.row');
//             let nextIndex = $indieDateRows.length - 1;
//             let $newDateRow = $baseClone.clone();
//             let $newDateInput = $newDateRow.find('input');
//             let newId = $newDateInput
//                 .attr('id', addIndex(nextIndex))
//                 .attr('name', addIndex(nextIndex))
//                 .attr('id');
//
//             $newDateRow.appendTo($individualDateContainer);
//             flatpickr('#' + newId);
//         });
//
//         $individualDateContainer.on('click', 'i', removeIndieDate);
//     });
// });

// function removeIndex(_, name) {
//     return name.slice(0, -1);
// }
//
// function addIndex(idx) {
//     return function (_, name) {
//         return name + idx;
//     }
// }
//
// function removeIndieDate(e) {
//     $(e.target).closest('.form-group.row').remove();
// }

