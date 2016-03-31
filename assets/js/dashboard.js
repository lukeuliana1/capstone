$ = jquery = Jquery = require("jquery");
require("jQuery-slimScroll");
Chart = require("Chart.js");
var githubdata = {};
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
        myPieChart = new Chart(ctx).Pie(data, {legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%>: <%%><%=segments[i].value%><%}%></li><%}%></ul>"
        });

        var legend = myPieChart.generateLegend();
        $("#legend").html(legend);
    });

   $.ajax({
        url: "https://api.github.com/repos/yeralin/capstone/stats/commit_activity",
        type: "GET"
    }).done(function(response){
        githubdata = response;
        var data1 = [];
        var i;
        console.log(githubdata);
        data1.push({ labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
            "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
            "51", "52"]});
        var info = [];
        var count = 0;
        for (i=0; i<githubdata.length; i++){
           for (j=0; j<githubdata[i].length; j++){
                count += githubdata[i];
            }
            info.push(count);
        }
        data1.push({
            data: info,
            strokeColor: getRandomColor(0),
            label: "Commit activity"
        });

        // Get context with jQuery - using jQuery's .get() method.
        ctx = $("#myChart").get(0).getContext("2d");
        // This will get the first returned node in the jQuery collection.
        //myLineChart = new Chart(ctx).Line(data1);

       //var legend = myLineChart.generateLegend();
       // $("#legend").html(legend);
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
