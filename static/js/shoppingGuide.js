
    let btnCollapse=$("#btn-collapse");
    let question   =$(".panel-question");
    let heading    =$(".panel-heading");
    let answer     =$(".panel-body");

    function activateQuestion(){
      answer.css({display:'none'});
      let activePanel =$(".panel-question.active .panel-body");
      activePanel.css({display :'block'});
    }

    heading.click(function(){
      question.removeClass('active');
      $(this).parent().addClass('active');
      activateQuestion();
    });
    btnCollapse.on('click',function(){
       answer.css({display:'none'});
    });
    activateQuestion();
