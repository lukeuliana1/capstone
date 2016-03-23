$ = jquery = Jquery = require("jquery");
require("slimScroll");
var fullpage = require("fullpage.js");

var removeActiveFromSections = function() {
    sectionsArray = [$(".description-section"), $(".team-section"), $(".sponsors-section"), $(".github-section"), $(".trello-section")];
    for(i=0; i < sectionsArray.length;i++){
        sectionsArray[i].removeClass("active");
    }
    return 0;
}

$(document).ready(function() {
    $('.slider').fullpage({
    	controlArrows: false,
    	loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false

    });

    var blocksArray = [$(".description-block"), $(".team-block"), $(".sponsors-block"), $(".github-block")];
    
    for(i=0; i < blocksArray.length; i++){
        blocksArray[i].slimScroll({
            height: '89%'
        });
    }

    $(".description-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 0);
        removeActiveFromSections();
        $(this).addClass("active");
    });
    $(".team-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 1);
        removeActiveFromSections();
        $(this).addClass("active");
    });
    $(".sponsors-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 2);
        removeActiveFromSections();
        $(this).addClass("active");
    });
    $(".github-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 3);
        removeActiveFromSections();
        $(this).addClass("active");
    });
    $(".trello-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 4);
        removeActiveFromSections();
        $(this).addClass("active");
    });
});