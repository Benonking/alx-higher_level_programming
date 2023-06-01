$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (res, status) {
    if (status === 'success') {
      $('DIV#hello').text(res.hello);
    }
  });
});
