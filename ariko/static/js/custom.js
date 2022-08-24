$(window).on('load', function() {
    "use strict";

    /*=========================================================================
        Preloader
    =========================================================================*/
    $("#preloader").delay(350).addClass('loaded');
    $('.site-wrapper').addClass('loaded');

    // Masonry
    var $container = $('.masonry');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: '.grid-item',
      });
    });

    // Infinite Scroll
    var curPage = 1;
    var pagesNum = $("#pagination-selector").find("li a:last").text();   // Number of pages

    $container.infinitescroll({
        itemSelector: '.grid-item',
        nextSelector: '.portfolio-pagination li a',
        navSelector: '#pagination-selector',
        extraScrollPx: 0,
        bufferPx: 0,
        maxPage: 6,
        loading: {
            finishedMsg: "No more works",
            msgText: '<div class="loader"><span></span></div>',
            speed: 'slow',
            selector: '.load-more',
        },
    },
    // trigger Masonry as a callback
    function( newElements ) {

      var $newElems = $( newElements );
      $newElems.imagesLoaded(function(){  
        // Append masonry
        $newElems.animate({ opacity: 1 });
        $container.masonry( 'appended', $newElems, true ); 
      });

      // Check last page
      curPage++;
      if(curPage == pagesNum) {
        $( '.load-more button' ).remove();
      }

      // Favorite button in retrieved posts
      $($newElems).on('click', ".favorite", function(){
          if ($(this).hasClass('ion-md-heart-empty')) {
              $(this).addClass('ion-md-heart');
              $(this).removeClass('ion-md-heart-empty');
              $(this).toggleClass('pulse');
          } else {
              $(this).addClass('ion-md-heart-empty');
              $(this).removeClass('ion-md-heart');
          }
      });
      $('.load-more').find('button').css('visibility', 'visible');
    });

    $container.infinitescroll( 'unbind' );

    $( '.load-more button' ).on('click', function() {
      $container.infinitescroll( 'retrieve' );
      $('.load-more').find('button').css('visibility', 'hidden');
      return false;
    });

    // Favorite posts
    favorite_post();

    function favorite_post()
    {
      $('.favorite').on('click', function() {
          if ($(this).hasClass('ion-md-heart-empty')) {
              $(this).addClass('ion-md-heart');
              $(this).removeClass('ion-md-heart-empty');
              $(this).toggleClass('pulse');
          } else {
              $(this).addClass('ion-md-heart-empty');
              $(this).removeClass('ion-md-heart');
          }
      }); 
    }

});

/*=========================================================================
            Home Slider
=========================================================================*/
$(document).on('ready', function() {
    "use strict";

    $('.slider').slick({
      dots: true,
      arrows: false,
    });

});

$(function(){
    "use strict";

    /*=========================================================================
            Overlay menu click
    =========================================================================*/
    $(".menu-icon").on( 'click', function() {
        $(".overlay-menu").addClass('opened');
    });

    $(".overlay-menu .close-icon").on( 'click', function() {
        $(".overlay-menu").removeClass('opened');
    });

    /*=========================================================================
     Parallax Image with Data Attribute
     =========================================================================*/
    var list = document.getElementsByClassName('parallax-bg');

    for (var i = 0; i < list.length; i++) {
      var src = list[i].getAttribute('data-image-src');
      list[i].style.backgroundImage="url('" + src + "')";
    }

    /*=========================================================================
     Parallax background images with Stellar JS
     =========================================================================*/
    $.stellar({
      horizontalScrolling: false,
      verticalOffset: 40
    });

    /*=========================================================================
            Main Menu
    =========================================================================*/
    $( ".submenu" ).before( '<i class="ion-md-add switch"></i>' );

    $(".vertical-menu li i.switch").on( 'click', function() {
        var $submenu = $(this).next(".submenu");
        $submenu.slideToggle(300);
        $submenu.parent().toggleClass("openmenu");
    });

    /*=========================================================================
            Scroll to Top
    =========================================================================*/
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 250) {        // If page is scrolled more than 50px
            $('#return-to-top').fadeIn(200);    // Fade in the arrow
        } else {
            $('#return-to-top').fadeOut(200);   // Else fade out the arrow
        }
    });
    $('#return-to-top').on('click', function() {      // When arrow is clicked
        $('body,html').animate({
            scrollTop : 0                       // Scroll to top of body
        }, 400);
    });

    $(document).on('mousemove', function(e){
  var width = $(document).width();
  var height = $(document).height();

  /*=========================================================================
          Styled cursor
  =========================================================================*/
  if(width > 990) {
      $('#cursor').css({'display':'block','left': Number((e.pageX)-10),'top': Number((e.pageY)-10),'z-index': '9999999'});
      if(Number((e.pageX)+24) > width) { $('#cursor').css({'display': 'none'}); }
      if(Number((e.pageX)) < 10) { $('#cursor').css({'display': 'none'}); }
      if(Number((e.pageY)+24) > height) { $('#cursor').css({'display': 'none'}); }
      if(Number((e.pageY)) < 10) { $('#cursor').css({'display': 'none'}); }

      $('a, .favorite, button, .menu-icon, .vertical-menu i, .close-icon').on('mouseenter',
        function(event) {
          $('#cursor').css({'transform':'scale(2.5)','border':'none','background':'rgba(0,0,0,0.1)'});
        }).on('mouseleave', function() {
          $('#cursor').css({'transform':'scale(1)','border':'3px #111 solid','background':'none'});
        }
      );
    }
  });

});