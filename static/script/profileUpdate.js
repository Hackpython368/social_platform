const profileUpdate = `<div class="overlay">
        
        <div class="upload-modal">
          
          <h3>Update Profile Data</h3>
          
          <!-- Upload Area -->
          
          <label class="upload-area">
            
            <input id="fileinput" type="file" hidden>
            
            <div class="upload-content">
              <div class="icon">⬆</div>
              <p><span>Drag & Drop</span> or <b>Choose file</b> to upload</p>
              <small>Supported formats: JPG or PNG</small>
            </div>
            
          </label>
          
          
          <!-- Bio Field -->
          
          <div class="bio-section">
            
            <label>Bio</label>
            <textarea id="bioinput" placeholder="Write short bio..."></textarea>
            
          </div>
          
          
          <!-- Buttons -->
          
          <div class="modal-buttons">
        
            <button class="cancel-btn" onclick=removeOverlay()>Cancel</button>
            <button class="upload-btn" onclick=updateProfile()>Upload</button>
            
          </div>
          
        </div>
      </div>`

let developerprofile = `<div class="overlay">
    <div class="card-container">
        <div class="close-btn" onclick="close()">X</div>
        <div class="card-structure">
            <div class="image" >
                
            </div>
            <div class="text">Hello I am Vidya Prakash Pandey Developer of the web application.</div>
            <div class="links">
                <a href="https://www.linkedin.com/in/vppandey368/">LinkedIn</a>
                <a href="https://github.com/hackpython368/">GitHub</a>
            </div>
        </div>
    </div>
    </div>`



profileUpdatebtn.addEventListener('click', () => {
  if (document.getElementById('overlay').innerHTML===""){
    document.getElementById('overlay').innerHTML += profileUpdate
  }
})

aboutBtn.addEventListener('click', () => {
  if (document.getElementById('overlay').innerHTML===""){
    document.getElementById('overlay').innerHTML += developerprofile
  }
})

document.getElementById('overlay').addEventListener('click',(e)=>{
  if(e.target.classList.contains('close-btn')){
    document.getElementById('overlay').innerHTML= ""
  }
  
})