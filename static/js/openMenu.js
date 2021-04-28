// hamburger 메뉴
$(document).ready(function(){
  $('.openMenu button.open').on('click', function(){
      $('.openMenu .menuWrap').addClass('on');
  });
  $('.openMenu .menuWrap .close').on('click', function(){
      $('.openMenu .menuWrap').removeClass('on');
  });
});




