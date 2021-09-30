$(document).ready(function () {
    $("#upl").click(function () {
        let formData = new FormData();
    formData.append("videoTitle", $("#name").val());
    formData.append("videoDesc", $("#videoDesc").val());
    formData.append("videoTags", $("#videoTags").val());
    formData.append("videoCat", $("#videoCat").val());
    let img=document.getElementById("imagee")
    let img1=img.files[0];
    formData.append("imagee",img1);
    let vdo=document.getElementById("videoo")
    let vdo1=vdo.files[0];
    formData.append("videoo",vdo1);
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
