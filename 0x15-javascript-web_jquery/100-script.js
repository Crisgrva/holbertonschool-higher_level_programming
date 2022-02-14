// Script that change color of element when page is loaded, without Jquery
window.addEventListener('load', function () {
  const header = this.document.querySelector('header');
  header.style.color = '#FF0000';
});
