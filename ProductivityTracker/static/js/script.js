// const progressBar = document.querySelector('.progress-bar');
// const progressValue = document.querySelector('.progress-value');

// function updateProgress() {
//   fetch('/task/completion_percentage/')  // Replace with your actual API endpoint URL
//     .then(response => response.json())
//     .then(data => {
//       const percentage = Math.round(data.completion_percentage);  // Round the percentage
//       progressValue.textContent = `${percentage}%`;
//       progressBar.style.transform = `rotate(${percentage * 1.8}deg)`;
//     })
//     .catch(error => console.error('Error fetching progress:', error));
// }

// updateProgress();  // Call initially to set the progress
