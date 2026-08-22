

const likepost = (post) => {
    fetch(`${url}/api/accounts/user/${post.id}/post/like/`, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        }
    }).then(res => res.json()).then(data => {
        if (data.code == "token_not_valid") {
            loadRefreshToken();
            likepost()

        } else {
            loadfeed()
        }
    })
}