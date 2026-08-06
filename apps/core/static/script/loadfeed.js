
const loadfeed = () => {
    fetch('http://127.0.0.1:8000/api/accounts/user/feed/', {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        }
    }).then(res => res.json()).then(data => {
        if (data.code == "token_not_valid") {
            loadRefreshToken();
            loadfeed();
        } else {
            // console.log(data)
            // localStorage.setItem('user_id', data['user_id'])
            document.getElementById("feed").innerHTML = ""
            for (let i = 0; data.data.length > i; i++) {

                document.getElementById("feed").innerHTML += `
              <div class="post" ondblclick="likepost(this)" id="${data['data'][i]['id']}">
              <div class="post-header">
                ${data['data'][i]['profile_pic'] == null ? `<div class="avatar" ><i class="fa-solid fa-user" style="font-size: 20px;"></i></div>` : `<div class="avatar" style="background-image: url(${data['data'][i]['profile_pic']}); background-size: cover;"></div>`}
                <!-- <div class="avatar" style="background-image: url(${data['data'][i]['profile_pic']})"></div> -->
                <div class="user-info">
                  <h4>${data['data'][i]['username']}</h4>
                  <span>12:30 pm · 2 Jan 2026</span>
                </div>
              </div>
              
              <div class="post-content">
                <p>${data['data'][i]['content'].replace('\n', '<br><br>')}</p>
              </div>
              ${data['data'][i]['post_img'] == null ? "" : `<img src="${data['data'][i]['post_img']}">`}
              
              
              <div id="rect-container" class="actions">
                <span class="like-btn">${data['data'][i]['liked'] == true ? `<i style="color:red" class="fa-solid fa-heart"></i>` : `<i class="fa-solid fa-heart"></i>`} ${data['data'][i]['like_count']}</span>
                <span id="comment">💬 ${data['data'][i]['comment_count']} Comment</span>
              </div>
              <div class="comment-txt"><input class="comment-text" type="text" placeholder="Comment...."><button class="comment-btn">Comment</button></div>
              
              <div class="comment-preview">
                ${data['data'][i]['latest_comment'] == null ? `` : `<strong>${data['data'][i]['latest_comment']['username']}</strong> ${data['data'][i]['latest_comment']['comment_text']}`}
              </div>
              
            </div>`
            }
        }

    })
}

loadfeed()