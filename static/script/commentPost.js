

function commentPost(comment_txt, p_id) {
    if(comment_txt){

        fetch(`${url}/api/accounts/user/${p_id}/post/comment/`, {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("access"),
                "Content-Type": "application/json"
        },
        body: JSON.stringify({
            'comment_text': comment_txt
        })
    }).then(res => res.json()).then(data => {
        if (data.code == "token_not_valid") {
            loadRefreshToken();
            likepost();
            
        } else {
            loadfeed()
        }
    })
}else{
    alert("Empty Comment!! Error");
}

}