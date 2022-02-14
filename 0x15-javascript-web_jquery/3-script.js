$(document).ready(function () {
  $('DIV#red_header').on('click', function (event) {
    $(event.delegateTarget).addClass('red');
  });
});
