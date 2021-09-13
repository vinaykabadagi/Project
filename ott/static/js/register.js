
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
