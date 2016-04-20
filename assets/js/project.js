$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
var githubdata = {};
Chart = require("Chart.js");
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

});

$.ajax({
        url: "https://api.github.com/repos/yeralin/capstone/stats/contributors",
        type: "GET"
    })
    .done(function(response) {
        $(".loading.first").addClass("hidden");
        $(".chartBox.first").removeClass("hidden");
        var githubdata = response;
        var dataPieChart = [];
        for (var i = 0; i < githubdata.length; i++) {
            dataPieChart.push({
                value: (githubdata[i]).total,
                color: getRandomColor(i),
                label: githubdata[i].author.login
            });
        }
        var ctx = $("#teamCommitsChart").get(0).getContext("2d");
        var githubPieChart = new Chart(ctx).Pie(dataPieChart, {legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%>: <%%><%=segments[i].value%><%}%></li><%}%></ul>"});
        var legend = githubPieChart.generateLegend();
        $("#legend").html(legend);
    }).fail(function() {
        $(".loading.first").addClass("hidden");
        $(".failResponseGithub.first").removeClass("hidden");
        $(".failResponseGithub.first").html("Server doesn't respond. <br> Check you settings.");
    });

$.ajax({
    url: "https://api.github.com/repos/yeralin/capstone/stats/commit_activity",
    type: "GET"
}).done(function(response) {
    $(".loading.second").addClass("hidden");
    $(".chartBox.second").removeClass("hidden");
    githubdata = response;
    var dataLineChart = [];
    var months = [];
    var info = [];
    var cnt = 0;
    var tempDate = new Date(githubdata[0].week);
    var currMonth = tempDate.getMonth();
    var curYear = tempDate.getYear();
    for(var i=0; i < githubdata.length; i++) {
        var thisDate = new Date(githubdata[i].week * 1000);
        if (thisDate.getMonth() == currMonth && thisDate.getYear() == curYear) {
            cnt += githubdata[i].total;
        } else {
            if (curYear != 70) {
                var m = findMonth(currMonth);
                months.push(m);
                info.push(cnt);
            }
            cnt = 0;
            currMonth = thisDate.getMonth();
            curYear = thisDate.getYear();
        }
    }
    dataLineChart = {
        labels: months,
        datasets: [{
            data: info,
            fillColor: '#018BBB',
            strokeColor: '#00374A',
            pointColor: '#00374A',
            pointStrokeColor: '#00374A',
            pointHighlightFill: '#018BBB',
            pointHighlightStroke: '#018BBB',
            label: "Commit activity"
        }]
    };
    var ctx = $("#totalCommitsChart").get(0).getContext("2d");
    var gitLineChart = new Chart(ctx).Line(dataLineChart, { showXLabels: 12 });
}).fail(function() {
    $(".loading.second").addClass("hidden");
    $(".failResponseGithub.second").removeClass("hidden");
    $(".failResponseGithub.second").html("Server doesn't respond. <br> Check you settings.");
});


var color_array = ['#018BBB', '#00374A', '#4DADCF', '#006182', '#B2DCEA', '#344653', '#B3B9BE', '#67747E', '#000000', '#E5F3F8'];
function getRandomColor(x) {
    //Keep poping precreated colors from array
    if (typeof x !== "undefined") {
        return color_array.splice(x,1)[0];
    }
    else if (color_array.length !== 0){
        return color_array.pop();
    }
    else { //If precreated colors array is empty, generate random color
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
    return -1; //should never happen
}

var monthArray = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
function findMonth(x) {
    return monthArray[x];
}