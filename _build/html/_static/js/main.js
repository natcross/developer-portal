$(document).ready(function() {
  $('#myTab a').click(function (e) {
    e.preventDefault()
    language = $(this).attr('href').substring(1).toLowerCase();    
    $('.codebox-tab').removeClass('active');
    $('.codebox-tab-'+language).addClass('active');
    $('.code').hide();
    $('.code-'+language).show();
  });

  $('#api-documentation > .row .examples .code-box .nav').affix({
    offset: 10
  })  
});