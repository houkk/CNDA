/**
 * Created by Mesogene on 2015/5/10.
 */
$(function(){
    $(".nav-button").click(function () {
        if ($('.in_navigation').hasClass("isDown")) {
            showmenu();

        } else {
            hidemenu();
        }
        return false;
    });


// flexslider  --------
    $('.serviseslider').flexslider({
        animation: "slide",
        smoothHeight: true,
        slideshow: false,
        controlNav: false,
        directionNav: false,
        startAt: 1,
        start: function (slider) {
            $('a.animbox').hover(function () {
                var slideTo = $(this).attr("name")
                var slideToInt = parseInt(slideTo)
                var ww = $(window).width();
                if (slider.currentSlide != slideToInt) {
                    slider.flexAnimate(slideToInt)
                }
                if (ww < 959) {
                    setTimeout(function () {
                        $('html').scrollTo('.serviseslider', 800, {'axis': 'y'});
                    }, 600);
                }
            });
        }
    });
    $('a.animbox').hover(function () {
        $('.service_box').removeClass('actser');
        $(this).parent().addClass('actser');
    });

    $(document.body).on('appear', '.service_box', function () {
        $(this).each(function () {
            $('.service_box').animate({opacity: '1', top: '0'}, {queue: true, duration: 1200});

        });
    });
    $('.moreinfo').hover(function () {
        var cursl = $(this);
        var th = $(this).find('div.member-skils');
        if ($(this).hasClass("notvisible")) {
            th.stop(true, true).animate({'top': '0'}, {queue: true, duration: 700, easing: "easeInOutQuad"});
            cursl.removeClass('notvisible');
        } else {
            th.animate({'top': '100%'});
            cursl.addClass('notvisible');
        }
        return false;

    });

// Contact submit  ----------------------------------------

    $("#submit_btn").click(function () {
        var user_name = $('input[name=name]').val();
        var user_email = $('input[name=email]').val();
        var user_message = $('textarea[name=message]').val();
        var proceed = true;
        if (user_name == "") {
            $('input[name=name]').css('border', '1px solid #F54F36');
            proceed = false
        }
        if (user_email == "") {
            $('input[name=email]').css('border', '1px solid #F54F36');
            proceed = false
        }
        if (user_message == "") {
            $('textarea[name=message]').css('border', '1px solid #F54F36');
            proceed = false
        }
        if (proceed) {
            post_data = {'userName': user_name, 'userEmail': user_email, 'userMessage': user_message};
            $.post('php/contact_me.php',
                post_data,
                function (data) {
                    $("#result").hide().html('<div class="success">' + data + '</div>').slideDown(500);
                    $('#contact_form input').val('');
                    $('#contact_form textarea').val('')
                }).fail(
                function (err) {
                    $("#result").hide().html('<div class="error">' + err.statusText + '</div>').fadeIn(1500)
                });
        }
    });
    $('.to-top').click(function () {
        $('html').scrollTo('#in_top', 1500, {'axis': 'y'});
        hidemenu();
    });
    $('#header_1').click(function () {
        $('html').scrollTo('#in_top', 1500, {'axis': 'y'});
        hidemenu();
    });
    $('#header_2').click(function () {
        $('html').scrollTo('#in_middle', 1500, {'axis': 'y'});
        hidemenu();
    });
    $('#header_3').click(function () {
        $('html').scrollTo('#in_contact', 1500, {'axis': 'y'});
        hidemenu();
    });
});

function showmenu() {
    var ino = $('.in_navigation');
    var ct = $('.link-holder a').length;
    var $tElems = $('.link-holder a');
    var al = {queue: true, duration: 800, easing: "easeInOutQuad"};
    $(".nav-button").addClass('nav-rotade');
    ino.removeClass("isDown");
    ino.animate({"right": '0px'}, al);
    setTimeout(function () {
        for (var i = 0; i <= ct; i++) {
            var cft = $tElems[i];
            $(cft).delay(150 * i).animate({'opacity': '1', left: '0'}, al);
        }
    }, 100);
}

function changePage(url){
    window.location.href=url;
}

// hide menu ------------------
function hidemenu() {
    var $tElems = $('.link-holder a');
    var ino = $('.in_navigation');
    var al = {queue: true, duration: 800, easing: "easeInOutQuad"};
    var ct = $('.link-holder a').length;
    $(".nav-button").removeClass('nav-rotade');
    ino.addClass("isDown");
    ino.animate({"right": '-200px'}, al);
    setTimeout(function () {
        for (var i = 0; i <= ct; i++) {
            var cft = $tElems[i];
            $(cft).delay(150 * i).animate({'opacity': '0', left: '-25%'}, al);
        }
    }, 100);
}

