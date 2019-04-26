jQuery(function ($) {
    // Initialize flatpickr for page inputs
    flatpickr('.flatpickr');

    let $individualDateContainer = $('#individual-date-container');
    let $baseClone = $individualDateContainer.find('.row').clone();

    $baseClone
        .find('input')
        .attr('id', removeIndex)
        .attr('name', removeIndex)
        .val('');

    $('#add-date').on('click', function (e) {
        e.preventDefault();
        let $indieDateRows = $individualDateContainer.find('.row');
        let nextIndex = $indieDateRows.length;
        let $newDateRow = $baseClone.clone();
        let $newDateInput = $newDateRow.find('input');
        let newId = $newDateInput
            .attr('id', addIndex(nextIndex))
            .attr('name', addIndex(nextIndex))
            .attr('id');

        $newDateRow.appendTo($individualDateContainer);
        flatpickr('#' + newId);
    });

    $individualDateContainer.on('click', 'i', removeIndieDate);
});

function removeIndex(_, name) {
    return name.slice(0, -1);
}

function addIndex(idx) {
    return function (_, name) {
        return name + idx;
    }
}

function removeIndieDate(e) {
    $(e.target).closest('.form-group.row').remove();
}