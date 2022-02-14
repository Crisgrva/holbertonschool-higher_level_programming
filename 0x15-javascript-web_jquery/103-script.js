// Script that fetch API that says hello in several languajes and add presskey event
$(document).ready(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=';

  $('INPUT#btn_translate').click(function () {
    const value = $('INPUT#language_code').val();
    $.get(URL + value, function (data) {
      if (data.code === '' || data.code === 'none') {
        alert('Supported languages is ar, az, be, bg, bn, bs, cs, da, de, dz, el, en, en-gb, en-us, es, et, fa, fi, fil, fr, he, hi, hr, hu, hy, id, is, it, ja, ka, kk, km, ko, lb, lo, lt, lv, mk, mn, ms, my, ne, no, pl, pt, ro, ru, sk, sl, sq, sr, sv, sw, th, tk, uk, vi, zh');
      } else {
        $('DIV#hello').text(data.hello);
      }
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      const value = $('INPUT#language_code').val();
      $.get(URL + value, function (data) {
        if (data.code === '' || data.code === 'none') {
          alert('Supported languages is ar, az, be, bg, bn, bs, cs, da, de, dz, el, en, en-gb, en-us, es, et, fa, fi, fil, fr, he, hi, hr, hu, hy, id, is, it, ja, ka, kk, km, ko, lb, lo, lt, lv, mk, mn, ms, my, ne, no, pl, pt, ro, ru, sk, sl, sq, sr, sv, sw, th, tk, uk, vi, zh');
        } else {
          $('DIV#hello').text(data.hello);
        }
      });
    }
  });
});
