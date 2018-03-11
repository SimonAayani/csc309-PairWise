
$('.menu .item')
  .tab()
;

$('.ui.search')
  .search({
    fields: {
      results : 'items',
      title   : 'name',
    },
    minCharacters : 3
  })
;