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
  });