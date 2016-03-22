$ = jquery = Jquery = require("jquery");
require("slimScroll");
var fullpage = require("fullpage.js");

$(document).ready(function() {
    $('.slider').fullpage({
    	controlArrows: false,
    	loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false

    });

    /*var blockedArray = [$(".description-block"), $(".team-block"), $(".sponsors-block"), $(".github-block")];
    for(i=0; i < blockedArray.size(); i++){
        blockedArray[i].slimScroll({
            height: '89%'
        });
    }*/
    $(".description-block").slimScroll({
        height: '89%'
    });

    $(".team-block").slimScroll({
        height: '89%'
    });

    $(".sponsors-block").slimScroll({
        height: '89%'
    });

    $(".github-block").slimScroll({
        height: '89%'
    });

    $(".description-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 0);
    });
    $(".team-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 1);
    });
    
});