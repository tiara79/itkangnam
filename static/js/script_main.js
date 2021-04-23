
// scroll animation
$(function(){
  $('.animation').scrolla({
    mobile: true,  // 모바일에서 동작함
    once: true    // 한 번만 동작함
  });
});

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

// 마우를 올리거나 포커스할 때 밑줄 효과 : span.bar
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



