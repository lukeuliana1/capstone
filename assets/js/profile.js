$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
fullpage = require("fullpage.js");

$(document).ready(function() {
	var activeBlock = $(".profile-section");
	var blocksArray = [$(".profile-block")];
    $('.slider').fullpage({
        controlArrows: false,
        loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false
    });
    $(".dashboard-container").scrollTop();
    for(i=0; i < blocksArray.length; i++){
        blocksArray[i].slimScroll({
            height: '92%'
        });
    }
    /*$(".description-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 0);
        activeBlock_project.removeClass("active");
        $(this).addClass("active");
        activeBlock_project = $(this);
    });*/

});