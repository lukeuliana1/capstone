$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
fullpage = require("fullpage.js");

$(document).ready(function() {
	var activeBlock = $(".current_projects-section");
	var blocksArray = [$(".current_projects-block"), $(".school-block"), $(".slack-block")];
    $('.slider').fullpage({
        controlArrows: false,
        loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false
    });
    $(".dashboard-container").bind("scroll", function() {
        if($(this).scrollTop() === 0) { 
            $("a.active").removeClass("scrolled");
        }
        else {
            $("a.active").addClass("scrolled")
        }
    });
    $(".dashboard-container").scrollTop();
    for(i=0; i < blocksArray.length; i++){
        blocksArray[i].slimScroll({
            height: '92%'
        });
    }
    $(".current_projects-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 0);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".school-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 1);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".slack-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 2);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });

});

