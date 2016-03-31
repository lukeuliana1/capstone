$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
var fullpage = require("fullpage.js");

$(document).ready(function() {
    activeBlock = $(".description-section");
    blocksArray = [$(".description-block"), $(".team-block"), $(".sponsors-block"), $(".github-block"), $(".trello-block")];
    $('.slider').fullpage({
    	controlArrows: false,
    	loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false

    });
    
    for(i=0; i < blocksArray.length; i++){
        blocksArray[i].slimScroll({
            height: '89%'
        });
    }

    $(".description-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 0);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".team-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 1);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".sponsors-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 2);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".github-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 3);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
    $(".trello-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 4);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });
});