$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
Chart = require("Chart.js");
var githubdata = {};
var fullpage = require("fullpage.js");


$(document).ready(function() {
    activeBlock = $(".description-section");
    blocksArray = [$(".description-block"), $(".team-block"), $(".sponsors-block"), $(".github-block"), $(".trello-block"), $(".profile-block")];
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
    }).done(function(response){
        githubdata = response;
        var data = [];
        var i;

        for (i=0; i<githubdata.length; i++){
           data.push({
            value: (githubdata[i]).total,
            color: getRandomColor(i),
            label: githubdata[i].author.login
            });
        }
        // Get context with jQuery - using jQuery's .get() method.
        ctx = $("#myChart").get(0).getContext("2d");
        // This will get the first returned node in the jQuery collection.
        myPieChart = new Chart(ctx).Pie(data, {legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%>: <%%><%=segments[i].value%><%}%></li><%}%></ul>"});

        var legend = myPieChart.generateLegend();
        $("#legend").html(legend);
    });

   $.ajax({
        url: "https://api.github.com/repos/yeralin/capstone/stats/commit_activity",
        type: "GET"
    }).done(function(response){
        githubdata = response;
        var data1 = [];
        var months = [];
        var i = 0;
        var info = [];
        var cnt = 0;
        var tempDate = new Date(githubdata[0].week);
        var currMonth = tempDate.getMonth();
        var curYear = tempDate.getYear();
        while (i<githubdata.length){           
            var thisDate = new Date(githubdata[i].week*1000);
            if (thisDate.getMonth() == currMonth && thisDate.getYear() == curYear){
                cnt += githubdata[i].total;
            }
            else{
                if (curYear!= 70){
                    var m = findMonth(currMonth);
                    months.push(m);
                    info.push(cnt);
                }                
                cnt = 0;
                currMonth = thisDate.getMonth();
                curYear = thisDate.getYear();
            }
            i++;                
        }
        data1 = { 
            labels: months,
            datasets: [
            {
                data: info,
                fillColor: getRandomColor(0),
                strokeColor: getRandomColor(1),
                pointColor: getRandomColor(1),
                pointStrokeColor: getRandomColor(1),
                pointHighlightFill: getRandomColor(0),
                pointHighlightStroke: getRandomColor(0),
                label: "Commit activity"
            }]};

        // Get context with jQuery - using jQuery's .get() method.
        ctx = $("#myLineChart").get(0).getContext("2d");
        // This will get the first returned node in the jQuery collection.
        myLineChart = new Chart(ctx).Line(data1, {showXLabels: 12});
    });


color_array = ['#018BBB', '#00374A', '#4DADCF', '#006182', '#B2DCEA', '#344653', '#B3B9BE', '#67747E', '#000000', '#E5F3F8'];

function getRandomColor(j) {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    if (j < 20)
        return color_array[j];
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function findMonth(x){
        var j;
        var curMonth = x;
        if (curMonth == 0){
             return ("January");
        }
        if (curMonth == 1){
             return ("February");
        }
        if (curMonth == 2){
             return ("March");
        }
        if (curMonth == 3){
             return ("April");
        }
        if (curMonth == 4){
             return ("May");
        }
        if (curMonth == 5){
             return ("June");
        }
        if (curMonth == 6){
             return ("July");
        }
        if (curMonth == 7){
             return ("August");
        }
        if (curMonth == 8){
             return ("September");
        }
        if (curMonth == 9){
             return ("October");
        }
        if (curMonth == 10){
             return ("November");
        }
        if (curMonth == 11){
             return ("December");
        }           
}
