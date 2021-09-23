// $(document).ready(function() {
//    $("#form").validate();
// });

$(document).ready(function () {
  $("#btnId").click(function () {
    if ($("#name").val() == "") {
      alert("Please Enter Name");
      return false;
    }
    if ($("#username").val() == "") {
      alert("Please Enter Username");
      return false;
    }
    if ($("#email-id").val() == "") {
      alert("Please Enter Email-id");
      return false;
    }
    if ($("#phoneno").val() == "") {
      alert("Please Enter Phone Number");
      return false;
    }
    if ($("#password").val() == "") {
      alert("Please Enter Password");
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
