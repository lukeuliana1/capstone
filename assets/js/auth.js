jQuery = jquery = $ = require("jquery");
require("flip");
csrfToken = require("./requires/csrfToken.js");
require("bootstrap-sass");
require("bootstrap-select");
csrftoken = csrfToken.getCookie('csrftoken');
register = false || 'default';

ajaxRequest = function() {
        var caller = $(event.currentTarget);
        $(".response").html("");
        if(caller.hasClass("sign-in-form")) {
            var ajaxProc = {
                urlPost : "/account/login/",
                redirect : "/account/profile/",
                form : $(".sign-in-form"),
                response : $("#front-response"),
                successMessage : "You are logged in"
            };
        }
        else if(caller.hasClass("reverse-form") && register) {
            var ajaxProc = {
                urlPost : "/account/register/",
                redirect : "/account/profile/",
                form : $(".reverse-form"),
                response : $("#reverse-response"),
                successMessage : "You are successfully registered."
            };

        }
        else if(caller.hasClass("reverse-form") && !register) {
            var ajaxProc = {
                urlPost : "/account/forgot-password/",
                redirect : "/account/profile/",
                form : $(".reverse-form"),
                response : $("#reverse-response"),
                successMessage : "Link has been sent to your email"
            };

        }
        else {
            console.error("Wrong request");
            return;
        }
        $.ajax({
            url: ajaxProc.urlPost,
            type: 'POST',
            data: ajaxProc.form.serialize(),
            beforeSend: function(xhr, settings) {
                $(".submit-button").addClass("disabled");
                $(".submit-button").prop("disabled", true);
                $(".submit-button").val("Loading...");
                if (!csrfToken.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }).done(function(response) {
            if (response == "success") {
                ajaxProc.response.css("color", "#3fa565");
                ajaxProc.response.append(ajaxProc.successMessage);
                $(".submit-button").val("Success");
                setTimeout(function(){
                        window.location.href = ajaxProc.redirect;
                    }, 1000);
            } else {
                ajaxProc.response.css("color", "#B51612");
                $(".submit-button").removeClass("disabled");
                $(".submit-button").prop("disabled", false);
                $(".submit-button").val("Submit");
                for (key in response) {
                    if (response.hasOwnProperty(key)) {
                        ajaxProc.response.append(response[key]);
                    }
                }
            }
        }).fail(function(response) {
            ajaxProc.response.css("color", "#dd1e31");
            ajaxProc.response.append("Our server is not responding.");
            $(".submit-button").removeClass("disabled");
            $(".submit-button").prop("disabled", false);
            $(".submit-button").val("Submit");
        });
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

    $(".sign-in-form").submit(function (event) {
        event.preventDefault();
        ajaxRequest();
    });

    $(".reverse-form").submit(function (event) {
        event.preventDefault();
        ajaxRequest();
    });

});
