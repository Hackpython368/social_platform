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
profileUpdatebtn.addEventListener('click', () => {
    document.getElementById('overlay').innerHTML += profileUpdate
})