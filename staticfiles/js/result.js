const copyBtn = document.querySelector('.copy_btn');
const facebookShare = document.querySelector('.facebook_share');

const kakaoShare = document.querySelector('.kakao_share');
Kakao.init('1f7a70ed2e9d63f3495e5f7206857c98');
// Kakao.isInitialized();
// kakao developer에서 플랫폼 등록해야함(도메인 필요)

function sendLink(){
    let result_url = window.location.href;
    Kakao.Link.sendDefault({
        objectType:'feed',
        content:{
            title:'군생활 강도 측정기',
            description:'내 군생활 강도는?',
            imageUrl:'https://mbit.weniv.co.kr/static/img/mbit_thumbnail.png',
            link:{
                mobileWebUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
                webUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
            },
        },
        social:{
            likeCount:286,
            commentCount:45,
            sharedCount:845,
        },
        buttons:[
        {
            title:'결과 보러가기',
            link:{
                webUrl:result_url,
                mobileWebUrl:result_url,
            },
        },
        {
            title:'테스트 하러가기',
            link:{
                webUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
                mobileWebUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
            },
        },
        ],
    });
}


$(function(){
    let url = window.location.href
    let img = $('.result_img img').attr('src');
    
    $("meta[property='og\\:url']").attr('content',url)
    $("meta[property='og\\:image']").attr('content',image)
});

function copyUrl(){
    let tmp = document.createElement('input');
    let url = location.href;
    
    document.body.appendChild(tmp);
    tmp.value = url;
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);
    
    alert("URL이 복사되었습니다.");
}

function sharefacebook(){
    let url = location.href;
    let facebook = 'http://www.facebook.com/sharer/sharer.php?u=';
    let link = facebook + url;
    window.open(link);
    
}

copyBtn.addEventListener('click', copyUrl);
facebookShare.addEventListener('click', sharefacebook);
kakaoShare.addEventListener('click', sendLink);