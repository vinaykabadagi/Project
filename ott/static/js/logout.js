$(document).ready(function () {
  $("#logout").click(function () {
    $.ajax({
      url: "/user_logout/",
      success: function (response) {
        if (response == "29") {
          alert("Logged Out");
          window.location = "/home/";
        }
      },
    });
  });
});
