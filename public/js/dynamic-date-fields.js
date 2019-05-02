// jQuery(function ($) {
//     let $dateFields = $('.date-fields');
//
//     let $dateFieldClone = $dateFields.find('div').first().clone();
//
//     console.log($dateFieldClone);
//
//     let prefix = 'a';
//
//     $('.date-field--add').on('click', function () {
//         prefix = String.fromCharCode(prefix.charCodeAt(0) + 1);
//         $clone = $dateFieldClone.clone();
//         $clone
//             .find('select[id*=exp_date]')
//             .each(function (i, el) {
//                 let $el = $(el);
//                 let newId = $el.attr('id').replace(/_._/, '_' + prefix + '_');
//                 let newName = $el.attr('name').replace(/^./, prefix);
//                 $(el).attr('id', newId);
//                 $(el).attr('name', newName);
//             });
//
//         $clone.appendTo($dateFields);
//     });
//
//     $dateFields.on('click', function (e) {
//         if ($(e.target).hasClass('date-field--remove')) {
//             $(e.target).closest('div').remove()
//         }
//     })
// });