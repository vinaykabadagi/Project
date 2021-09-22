
// $(document).ready(function() {
//    $("#form").validate();
// });

$(document).ready(function() {
	$("#btnId").click(function(){
		if($("#name").val() == "") {
			alert("Please Enter Name");
		}
		if($("#email-id").val() == "") {
			alert("Please Enter Email-id");
		}
		if($("#phoneno").val() == "") {
			alert("Please Enter Phone Number");
		}
		if($("#password").val() == "") {
			alert("Please Enter Password");
		}
		if($("#confirmpassword").val() == "") {
			alert("Please Confirm your Password");
		}

	});
});

let formData=new FormData();
formData.append("name",$("#name").val());
formData.append("email-id",$("#email-id").val());
formData.append("phoneno",$("#phoneno").val());
formData.append("password",$("#password").val());
formData.append("confirmpassword",$("#confirmpassword").val());

$.ajax ({
	url:"/user_reg/",urls unique
	type:"POST",
	data:formData,
	proconData:false,
	contentType:false,
	success;function(response){
		alert("Registration successful");

	}
	error function(error){

	}
})