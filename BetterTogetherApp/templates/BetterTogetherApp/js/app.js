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