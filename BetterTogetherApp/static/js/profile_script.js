function pasuser(form) {
    if (form.id.value == "1") {
      if (form.pass.value == "2") {
        location = "profile.html"
      } else {
        alert("Invalid Password")
      }
    } else {
      alert("Invalid UserID")
    }
  }


  $("#profileImage").click(function(e) {
    $("#imageUpload").click();
});

function fasterPreview( uploader ) {
    if ( uploader.files && uploader.files[0] ){
          $('#profileImage').attr('src', 
             window.URL.createObjectURL(uploader.files[0]) );
    }
}

$("#imageUpload").change(function(){
    fasterPreview( this );
});