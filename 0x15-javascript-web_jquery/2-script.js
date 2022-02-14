// Script that adds color to an element with Jquery
$(document).ready(function () {
  $('DIV#red_header').on('click', function (event) {
    $(event.delegateTarget).css('color', '#FF0000');
  });
});
