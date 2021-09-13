$(document).ready(function() {
	$("#login").click(function(){
		if($("#name").val() == "") {
			alert("Please Enter Name");
		}
		if($("#password").val() == "") {
			alert("Please Enter Password");
		}});
});