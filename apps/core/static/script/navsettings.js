const settingsBtn = document.getElementById("settingsBtn")
const settingsMenu = document.getElementById("settingsMenu")
const closeBtn = document.getElementById("closeBtn")
const themeToggle = document.getElementById("themeToggle")
const profileUpdatebtn = document.getElementById('profileUpdatebtn')

/* Toggle menu */

settingsBtn.addEventListener("click", () => {

    settingsMenu.classList.toggle("active")

})

/* Close button */

closeBtn.addEventListener("click", () => {
    settingsMenu.classList.remove("active")

})

/* Click outside */

document.addEventListener("click", (e) => {

    if (!settingsMenu.contains(e.target) && !settingsBtn.contains(e.target)) {

        settingsMenu.classList.remove("active")

    }

})


console.log("This is first log")



const updateProfile = () =>{

    const formdata = new FormData()
    const fileinput = document.getElementById('fileinput')
    const bioinput = document.getElementById('bioinput')


    formdata.append('bio',bioinput.value)
    formdata.append('profile_pic',fileinput.files[0])

    fetch('http://127.0.0.1:8000/api/accounts/profile/',{
      method: "POST",
      headers: {
              "Authorization": "Bearer " + localStorage.getItem("access")
            },
      body : formdata
    }).then(res =>res.json()).then(data => {
      console.log(data)
    })
  }






if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add("dark-theme");
} else {
    document.body.classList.add("light-theme");
}



themeToggle.addEventListener('change', () => {
    document.body.classList.toggle('dark-theme')
})