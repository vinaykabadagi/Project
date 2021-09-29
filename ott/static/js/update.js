$(document).ready(function () {
  $("#vinay").click(function () {
    let usernameValue = $("#username").val();
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    let patt = /^[A-Za-z0-9]+$/;
    let s = $("#email-id").val();
    if ($("#name").val() == "") {
      alert("Please Enter Name");
      return false;
    }
    if ($("#username").val() == "") {
      alert("Please Enter Username");
      return false;
    } else if (
      usernameValue.length < 3 ||
      usernameValue.length > 10 ||
      patt.test(usernameValue) == 0
    ) {
      alert(
        "**length of username must be between 3 and 10 **no special charactrers"
      );
      return false;
    }
    if ($("#email-id").val() == "" || regex.test(s) == 0) {
      alert("Please Enter valid Email-id");
      return false;
    }
    let formData = new FormData();
    formData.append("name", $("#name").val());
    formData.append("username", $("#username").val());
    formData.append("email-id", $("#email-id").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );

    $.ajax({
      url: "/user_update/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        window.location = "/home/";
      },
    });
  });

  $("#vinay1").click(function () {
    let pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;

    if ($("#newpassword").val() == "") {
      alert("Please Enter Password");
      return false;
    } else if (
      $("#newpassword").val().length < 5 ||
      pattern.test($("#newpassword").val()) == 0
    ) {
      alert(
        "Must contain at least one  number and one uppercase and lowercase letter, and at least 8 or more characters"
      );
      return false;
    }

    if ($("#confirmpassword").val() == "") {
      alert("Please Confirm your Password");
      return false;
    }

    if ($("#confirmpassword").val() != $("#newpassword").val()) {
      alert($("#confirmpassword").val())
      alert("Please Enter Password and Confirm Password Same");
      return false;
    }

    let formData = new FormData();
    formData.append("password", $("#password").val());
    formData.append("newpassword", $("#newpassword").val());
    formData.append("confirmpassword", $("#confirmpassword").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );

    $.ajax({
      url: "/update_password/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        window.location = "/home/";
      },
    });
  });
});
