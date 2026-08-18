

function loadRefreshToken(){
    console.log(localStorage.getItem('refresh'));
    fetch(`${url}/api/token/refresh/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ refresh: localStorage.getItem('refresh') })
    }).then(res => res.json()).then(data => {
        localStorage.setItem('access', data.data.access)
    })
}