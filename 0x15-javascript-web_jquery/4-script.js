// Script that toggle between 2 classes with Jquery
$(document).ready(function () {
  const classes = ['red', 'green'];
  let switchs = 1;
  $('DIV#toggle_header').addClass(classes[switchs]);

  $('DIV#toggle_header').click(function () {
    $('DIV#toggle_header').removeClass(classes[switchs]);
    switchs === 1 ? switchs = 0 : switchs = 1;
    $('DIV#toggle_header').toggleClass(classes[switchs]);
  });
});
