// $(document).ready(function() {
//    $("#form").validate();
// });

$(document).ready(function () {
  $("#btnId").click(function () {
    let usernameValue = $("#username").val();
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
	let pattern= /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
	let patt= /[A-Za-z0-9]+/;
    let s = $("#email-id").val();
	let y = $("#password").val();
    if ($("#name").val() == "") {
      alert("Please Enter Name");
      return false;
    }
    if ($("#username").val() == "") {
      alert("Please Enter Username");
      return false;
    } else if (usernameValue.length < 3 || usernameValue.length > 10|| patt.test(usernameValue) == 0) {
      alert("**length of username must be between 3 and 10");
      return false;
    }
    if ($("#email-id").val() == "" || regex.test(s) == 0) {
      alert("Please Enter valid Email-id");
      return false;
    }
    if ($("#phoneno").val() == "") {
      alert("Please Enter Phone Number");
      return false;
    }
    if ($("#password").val() == "") {
      alert("Please Enter Password");
      return false;
    } else if ($("#password").val().length < 5 || pattern.test(y) == 0) {
      alert("**length of password must be at least 5 or enter your password with validation");
      return false;
    }

    if ($("#confirmpassword").val() == "") {
      alert("Please Confirm your Password");
      return false;
    }

    if ($("#confirmpassword").val() != $("#password").val()) {
      alert("Please Enter Password and Confirm Password Same");
      return false;
    }

    let formData = new FormData();
    formData.append("name", $("#name").val());
    formData.append("username", $("#username").val());
    formData.append("email-id", $("#email-id").val());
    formData.append("phoneno", $("#phoneno").val());
    formData.append("password", $("#password").val());
    formData.append("confirmpassword", $("#confirmpassword").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );

    $.ajax({
      url: "/user_registeration/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        if (response == "10") {
          alert("Already Registered! LOGIN!");
          window.location = "/login/";
        } else {
          alert("Registration successful");
          window.location = "/home/";
        }
      },
    });
  });
});
