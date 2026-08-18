

function createPostModal() {

    const overlay = document.getElementById('overlay').innerHTML += `<div class="overlay">

  <div class="post-modal">

    <!-- LEFT SIDE (IMAGE UPLOAD) -->

    <div class="upload-section">

      <label class="upload-box">

        <input id="postimg" type="file" hidden>

        <div class="upload-content">
          <div class="upload-icon">📷</div>
          <p>Drag & Drop Image</p>
          <span>or Click to Upload</span>
        </div>

      </label>

    </div>


    <!-- RIGHT SIDE (POST CONTENT) -->

    <div class="content-section">

      <h3>Create Post</h3>

      <textarea id="posttext" placeholder="Write something about this post..."></textarea>

      <div class="buttons">

        <button class="cancel-btn" onclick=removeOverlay()>Cancel</button>
        <button class="post-btn" onclick=createPost()>Post</button>

      </div>

    </div>

  </div>

</div>
    `;




}

const createPost = () => {

    const formdata = new FormData()

    const file = document.getElementById('postimg').files[0]
    const text = document.getElementById('posttext').value

    if (file) {
        formdata.append('post_img', file)
    }

    if(text){
      formdata.append('content', text)

    }else{
      formdata.append('content',"")
    }


    fetch(`${url}/api/accounts/user/create/post/`, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        },
        body: formdata
    })
        .then(res => res.json())
        .then(data => {
          if(data.code == "token_not_valid"){
            loadRefreshToken()
            createPost()
          }else{

            console.log(data)
            removeOverlay()
          }
        })
}
document.getElementById("openPostModal").addEventListener("click", createPostModal);
document.getElementById("openPostModalMobile").addEventListener("click", createPostModal);
