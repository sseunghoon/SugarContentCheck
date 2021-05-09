function scrollUP(){
    const vheight = $('.test').height();
    $('html, body').animate({
        scrollTop:((Math.floor($(window).scrollTop() / vheight) - 1)*vheight)
    }, 500);
}

function scrollUP(){
    const vheight = $('.test').height();
    $('html, body').animate({
        scrollTop:((Math.floor($(window).scrollTop() / vheight) + 1)*vheight)
    }, 500);
}

$(function() {
    $('.next_btn').click(function(e){
        let divs = $(this).parent().prev().children()
        let inputs = divs.find('input:checked');
        if(inputs.length <1){
            alert('답변을 체크해주세요.');
            return false;
        }
        e.preventDefault();
        scrollDown();
    });
    
    $('.prev_btn').click(function(e){
        e.preventDefault();
        scrollUp();
    });
    
    $('#form').submit(function(e){
        let radios = $('input[type=radio]:checked');
        if(radios.length < 3){
            alert("모든 답변을 체크해주세요.");
            return false;
        }
        return true;
    });
    
    $('html, body').click(function(e){
        scrollTop:0;
    }, 500);
    
});