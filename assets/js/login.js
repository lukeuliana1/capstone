jQuery = jquery = $ = require("jquery");
csrfToken = require("./requires/csrfToken.js");
var register = false,
	csrftoken = csrfToken.getCookie('csrftoken');
$( document ).ready(function() {
	$(".signup").on( "click", function() {
		$(".first-name-group").show("slow");
		$(".last-name-group").show("slow");
		$(".bottomText.Up").fadeOut("slow", function(){
			$(".bottomText.In").fadeIn("slow");
		});
		register = true;

	});

	$(".signin").on( "click", function() {
		$(".first-name-group").hide("slow");
		$(".last-name-group").hide("slow");
		$(".bottomText.In").fadeOut("slow", function(){
			$(".bottomText.Up").fadeIn("slow");
		});
		register = false;
		
	});

	$(".auth").submit(function(event) {
        $(".response").html("");
        event.preventDefault();
        var urlPost;
        if (register) {
            urlPost = "/account/register/";
        } else {
            urlPost = "/account/login/";
        }
        $.ajax({
            url: urlPost,
            type: 'POST',
            data: $(".auth").serialize(),
            beforeSend: function(xhr, settings) {
                $(".loading").css("display", "block");
                if (!csrfToken.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }).done(function(response) {
            $(".loading").css("display", "none");
            if (response == "success") {
                $(".response").css("color", "#3fa565");
                if (register){
                    $(".response").append("You are successfully registered. <br> Wait till page refreshes");
                }
                else{
                    $(".response").append("You are logged in. <br> Wait till page refreshes");
                }
               	window.location.href = "/account/profile"
            } else {
                $(".response").css("color", "#dd1e31");
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        $(".response").append(response[key]);
                    }
                }
            }
        }).fail(function(response) {
        	$(".loading").css("display", "none");
        	$(".response").css("color", "#dd1e31");
            $(".response").append("Our server is not responding. Please try again later");
        });
    });

});
