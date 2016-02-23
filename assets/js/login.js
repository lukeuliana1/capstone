jQuery = jquery = $ = require("jquery");
require("flip");
csrfToken = require("./requires/csrfToken.js");
require("bootstrap-sass");
require("bootstrap-select");
csrftoken = csrfToken.getCookie('csrftoken'),
register = false || 'default';

var getVariable = function(){
    return register;
}

$( document ).ready(function() {

    $(".auth-block").flip({
        trigger:"manual"
    });

    $(".sign-up-toggle").on("click", function(){
        register = true;
        $(".sign-up-toggle").animate({opacity: 0.0}, 400, function(){
            $(".sign-up-toggle").css("visibility","hidden");
        });
        $(".reverse-side-label").text("Employee Account");
        $(".auth-block").flip('toggle');
    });
    $(".forgot-password").on("click", function(){
        register = false;
        $(".sign-up-toggle").animate({opacity: 0.0}, 400, function(){
            $(".sign-up-toggle").css("visibility","hidden");
        });
        $(".reverse-side-label").text("Restore Password");
        $(".auth-block").flip('toggle');
    });
    $(".go-back").on("click", function(){
        $(".sign-up-toggle").css({visibility:"visible", opacity: 0.0}).animate({opacity: 1.0},400);
        $(".auth-block").flip('toggle');
    });

    $(".reverse-form").submit(function(event) {
        event.preventDefault();
        $("#reverse-response").html("");
        var urlPost;
        if (register) {
            urlPost = "/account/register/";
        } else {
            urlPost = "/account/forgot-password/"; //not implemented yet
        }
        $.ajax({
            url: urlPost,
            type: 'POST',
            data: $(".reverse-form").serialize(),
            beforeSend: function(xhr, settings) {
                $(".sign-in-button").addClass("disabled");
                $(".sign-in-button").prop("disabled", true);
                $(".sign-in-button").val("Loading...");
                if (!csrfToken.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }).done(function(response) {
            $(".sign-in-button").removeClass("disabled");
            $(".sign-in-button").prop("disabled", false);
            $(".sign-in-button").val("Submit");
            if (response == "success") {
                $("#reverse-response").css("color", "#3fa565");
                if (register){
                    $("#reverse-response").append("You are successfully registered. <br> Wait till page refreshes");
                }
                else{
                    $("#reverse-response").append("You are logged in. <br> Wait till page refreshes");
                }
                window.location.href = "/account/profile";
            } else {
                $("#reverse-response").css("color", "#B51612");
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        $("#reverse-response").append(response[key]);
                    }
                }
            }
        }).fail(function(response) {
            $("#reverse-response").css("color", "#dd1e31");
            $("#reverse-response").append("Our server is not responding. Please try again later");
            $(".sign-in-button").removeClass("disabled");
            $(".sign-in-button").prop("disabled", false);
            $(".sign-in-button").val("Submit");
        });
    });


    $(".sign-in-form").submit(function(event) {
        $(".response").html("");
        event.preventDefault();
        $.ajax({
            url: "/account/login/",
            type: 'POST',
            data: $(".sign-in-form").serialize(),
            beforeSend: function(xhr, settings) {
                $(".sign-in-button").addClass("disabled");
                $(".sign-in-button").prop("disabled", true);
                $(".sign-in-button").val("Loading...");
                if (!csrfToken.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }).done(function(response) {
            $(".sign-in-button").removeClass("disabled");
            $(".sign-in-button").prop("disabled", false);
            $(".sign-in-button").val("Submit");
            if (response == "success") {
                $("#front-response").css("color", "#3fa565");
                if (register){
                    $("#front-response").append("You are successfully registered. <br> Wait till page refreshes");
                }
                else{
                    $("#front-response").append("You are logged in. <br> Wait till page refreshes");
                }
                window.location.href = "/account/profile"
            } else {
                $("#front-response").css("color", "#B51612");
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        $("#front-response").append(response[key]);
                    }
                }
            }
        }).fail(function(response) {
            $("#front-response").css("color", "#dd1e31");
            $("#front-response").append("Our server is not responding. Please try again later");
            $(".sign-in-button").removeClass("disabled");
            $(".sign-in-button").prop("disabled", false);
            $(".sign-in-button").val("Submit");
        });
    });

});
