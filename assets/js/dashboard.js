$ = jquery = Jquery = require("jquery");
require("slimScroll");
var fullpage = require("fullpage.js");

jQuery.fn.removeClassExcept = function (val) {
    return this.each(function (index, el) {
        var keep = val.split(" "),  // list we'd like to keep
        reAdd = [],          // ones that should be re-added if found
        $el = $(el);       // element we're working on
        // look for which we re-add (based on them already existing)
        for (var c = 0; c < keep.length; c++){
          if ($el.hasClass(keep[c])) reAdd.push(keep[c]);
        }

        // drop all, and only add those confirmed as existing
        $el
          .removeClass()               // remove existing classes
          .addClass(reAdd.join(' '));  // re-add the confirmed ones
    });
};

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
        $(".sub-nav").removeClassExcept("nav sub-nav");
        $(".sub-nav").addClass("first"); 
    });
    $(".team-section").on("click", function() {
    	$.fn.fullpage.moveTo(0, 1);
        $(".sub-nav").removeClassExcept("nav sub-nav");
        $(".sub-nav").addClass("second"); 
    });
    $(".sponsors-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 2);
        $(".sub-nav").removeClassExcept("nav sub-nav");
        $(".sub-nav").addClass("third"); 
    });
    $(".github-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 3);
        $(".sub-nav").removeClassExcept("nav sub-nav");
        $(".sub-nav").addClass("fourth"); 
    });
    
});