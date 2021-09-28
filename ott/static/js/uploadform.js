$(document).ready(function () {
    $("#upl").click(function () {
        let formData = new FormData();
    formData.append("videoTitle", $("#name").val());
    formData.append("videoDesc", $("#videoDesc").val());
    formData.append("videoTags", $("#videoTags").val());
    formData.append("videoCat", $("#videoCat").val());
    formData.append("videoImg", $("#videoImg").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    });

    $.ajax({
        url: "/user_registeration/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        
        });
});
