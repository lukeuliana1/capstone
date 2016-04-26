$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
var githubdata = {};
Chart = require("Chart.js");
githubApiStats = require("./requires/githubApi.js");
fullpage = require("fullpage.js");

$(document).ready(function() {
    var activeBlock = $(".description-section");
    var blocksArray = [$(".description-block"), $(".team-block"), $(".sponsors-block"), $(".github-block"), $(".trello-block"), $(".profile-block")];
    $('.slider').fullpage({
        controlArrows: false,
        loopHorizontal: false,
        keyboardScrolling: false,
        verticalCentered: false
    });
    $(".dashboard-container").bind("scroll", function() {
        if ($(this).scrollTop() === 0) {
            $("a.active").removeClass("scrolled");
        } else {
            $("a.active").addClass("scrolled")
        }
    });
    $(".dashboard-container").scrollTop();
    for (i = 0; i < blocksArray.length; i++) {
        blocksArray[i].slimScroll({
            height: '92%'
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
    $(".profile-section").on("click", function() {
        $.fn.fullpage.moveTo(0, 5);
        activeBlock.removeClass("active");
        $(this).addClass("active");
        activeBlock = $(this);
    });

    if(githubExists) {
        githubApiStats.init(githubRepoLink);
    }

});


