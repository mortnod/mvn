$(window).scroll(function(){

  var windowScroll = $(this).scrollTop();

  if (windowScroll < $('.js-section-about').offset().top) {
    var mountains = {
      left1: {
        translateX: -1*(windowScroll/80) + '%',
        scale: 1 + windowScroll/400
      },

      left2: {
        translateX: -1*(windowScroll/120) + '%',
        scale: 1 + windowScroll/500
      },
      middle: {
        translateX: 0,
        scale: 1 + windowScroll/400
      },
      right5: {
        translateX: windowScroll/200 + '%',
        scale: 1 + windowScroll/800
      },
      right4: {
        translateX: windowScroll/150 + '%',
        scale: 1 + windowScroll/600
      },
      right3: {
        translateX: windowScroll/120 + '%',
        scale: 1 + windowScroll/500
      },
      right2: {
        translateX: windowScroll/100 + '%',
        scale: 1 + windowScroll/450
      },
      right1: {
        translateX: windowScroll/80 + '%',
        scale: 1 + windowScroll/400
      },
    };

    function mountainTransform(selector, scale, translateX){
       var val = 'scale(' + scale + ') translateX(' + translateX + ')';
       $(selector).css({"-webkit-transform": val, "transform":val});
    }

    mountainTransform('.js-mountain-left-1', mountains.left1.scale, mountains.left1.translateX);
    mountainTransform('.js-mountain-left-2', mountains.left2.scale, mountains.left2.translateX);
    mountainTransform('.js-mountain-middle', mountains.middle.scale, mountains.middle.translateX);
    mountainTransform('.js-mountain-right-5', mountains.right5.scale, mountains.right5.translateX);
    mountainTransform('.js-mountain-right-4', mountains.right4.scale, mountains.right4.translateX);
    mountainTransform('.js-mountain-right-3', mountains.right3.scale, mountains.right3.translateX);
    mountainTransform('.js-mountain-right-2', mountains.right2.scale, mountains.right2.translateX);
    mountainTransform('.js-mountain-right-1', mountains.right1.scale, mountains.right1.translateX);

    $('.js-header-tagline').css('opacity', 1 - windowScroll*0.03);
  }
});
