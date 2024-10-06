// Search filter functionality
function filterVideos() {
    let input = document.getElementById('searchInput');
    let filter = input.value.toLowerCase();
    let videoItems = document.querySelectorAll('.video-item');
    
    videoItems.forEach((item) => {
      let title = item.querySelector('.card-title').textContent;
      if (title.toLowerCase().indexOf(filter) > -1) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }// Search filter functionality
function filterVideos() {
    let input = document.getElementById('searchInput');
    let filter = input.value.toLowerCase();
    let videoItems = document.querySelectorAll('.video-item');
    
    videoItems.forEach((item) => {
      let title = item.querySelector('.card-title').textContent;
      if (title.toLowerCase().indexOf(filter) > -1) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }