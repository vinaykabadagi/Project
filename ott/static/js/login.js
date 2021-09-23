$(document).ready(function() {
	$("#login").click(function(){
		if($("#name").val() == "") {
			alert("Please Enter Name");
		}
		if($("#password").val() == "") {
			alert("Please Enter Password");
		}

let formData = new FormData();
    formData.append("name", $("#name").val());
	formData.append("password", $("#password").val());
	formData.append(
		"csrfmiddlewaretoken",
		$("input[name=csrfmiddlewaretoken]").val()
	  );

$.ajax({
	url: "/user_login/",
	type: "POST",
	data: formData,
	processData: false,
	contentType: false,
	success: function (response) {
		alert("Login successful");
		window.location = "/home/";
	}
});
});
});