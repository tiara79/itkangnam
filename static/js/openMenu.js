// background-color change
$(window).on('scroll resize', function(){
  let scrollTop = $(document).scrollTop();
  bgColor();
  function bgColor(){
    if(scrollTop > 1400){
      $('body').addClass('on');
    }else{
      $('body').removeClass('on');
    }
    if(scrollTop > 2700){
      $('body').removeClass('on');
    }
  }
});

// hamburger 메뉴
$(function(){
  $('.openMenu button.open').on('click', function(){
      $('.openMenu .menuWrap').addClass('on');
  });
  $('.openMenu .menuWrap .close').on('click', function(){
      $('.openMenu .menuWrap').removeClass('on');
  });
});

$(function(){
  $('.gnb li a').on('mouseenter focus', function(){
    let bar = $(this).position().left;
    let widNum = $(this).width();
    $('span.bar').css({'left':bar + 'px', 'width':widNum + 'px', opacity:1});
  });
  $('.gnb li a').on('mouseleave', function(){
    $('span.bar').css({'left':0, 'width':0, opacity:0});
  });
});

