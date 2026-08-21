const settingsBtn = document.getElementById("settingsBtn")
const settingsMenu = document.getElementById("settingsMenu")
const closeBtn = document.getElementById("closeBtn")
const themeToggle = document.getElementById("themeToggle")
const profileUpdatebtn = document.getElementById('profileUpdatebtn')
const aboutBtn = document.getElementById('aboutBtn') 

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



const updateProfile = () => {

    const formdata = new FormData()
    const fileinput = document.getElementById('fileinput')
    const bioinput = document.getElementById('bioinput')


    formdata.append('bio', bioinput.value)
    formdata.append('profile_pic', fileinput.files[0])

    fetch(`${url}/api/accounts/profile/`, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        },
        body: formdata
    }).then(res => res.json()).then(data => {
        console.log(data)
    })
}






// if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
//     document.body.classList.add("dark-theme");
// } else {
//     document.body.classList.add("light-theme");
// }
const theme = localStorage.getItem('theme');
console.log(theme);
if (theme == "dark") {
    document.body.classList.add("dark-theme");
} else {
    document.body.classList.add("light-theme");
}


themeToggle.addEventListener('change', () => {
    const theme = localStorage.getItem('theme');

    if (theme != 'light') {
        localStorage.setItem('theme', 'light')
    } else {
        localStorage.setItem('theme', 'dark')
    }
    document.body.classList.toggle('dark-theme')
})