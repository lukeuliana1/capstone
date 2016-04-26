var color_array = ['#018BBB', '#00374A', '#4DADCF', '#006182', '#B2DCEA', '#344653', '#B3B9BE', '#67747E', '#000000', '#E5F3F8'];
var monthArray = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

function init(githubRepoLink) {

    $.ajax({
            url: "https://api.github.com/repos/"+githubRepoLink+"/stats/contributors",
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
            var githubPieChart = new Chart(ctx).Pie(dataPieChart);
            var legend = githubPieChart.generateLegend();
            $("#legend").html(legend);
        }).fail(function() {
            $(".loading.first").addClass("hidden");
            $(".failResponseGithub.first").removeClass("hidden");
            $(".failResponseGithub.first").html("Server doesn't respond. <br> Check you settings.");
        });

    $.ajax({
        url: "https://api.github.com/repos/"+githubRepoLink+"/stats/commit_activity",
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
        for (var i = 0; i < githubdata.length; i++) {
            var thisDate = new Date(githubdata[i].week * 1000);
            if (thisDate.getMonth() == currMonth && thisDate.getYear() == curYear) {
                cnt += githubdata[i].total;
            } else {
                if (curYear != 70) {
                    var m = monthArray[currMonth];
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
}

function getRandomColor(x) {
    //Keep poping precreated colors from array
    if (typeof x !== "undefined") {
        return color_array.splice(x, 1)[0];
    } else if (color_array.length !== 0) {
        return color_array.pop();
    } else { //If precreated colors array is empty, generate random color
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
    return -1; //should never happen
}

module.exports = {
    init: init
}
