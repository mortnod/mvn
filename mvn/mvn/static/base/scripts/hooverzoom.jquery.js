$(document).ready(function() {
    $('.viewport').mouseenter(function(e) {
        $(this).children('a').children('img').animate({ height: '322', left: '0', top: '0', width: '485'}, 100);
        $(this).children('a').children('span').fadeOut(200);
    }).mouseleave(function(e) {
        $(this).children('a').children('img').animate({ height: '349', left: '-20', top: '-20', width: '525'}, 100);
        $(this).children('a').children('span').fadeTo(100, 1);
        $(this).children('a').children('span').fadeIn(200);
    });
});