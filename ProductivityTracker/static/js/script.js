document.addEventListener("DOMContentLoaded", function() {
    fetch('/task/completion_percentage')
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data); // Log the response to debug
            const progressValue = parseFloat(data.completion_percentage).toFixed(2); // Ensure the value is a float and limit to 2 decimal places
            updateProgressBar(progressValue);
        })
        .catch(error => console.error('Error fetching progress:', error));
});

document.addEventListener("DOMContentLoaded", function() {
    // Generate a random integer between 1 and 22
    const randomInteger = Math.floor(Math.random() * 22) + 1;

    // Fetch the quote using the random integer
    fetch(`/quote/${randomInteger}/`)
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data); // Log the response to debug

            // Update the quote text and author
            document.querySelector('.quote-text').textContent = data.quote;
            document.querySelector('.blog-post-bottom').textContent = data.author;
        })
        .catch(error => console.error('Error fetching quote:', error));
});

const rightButtonImage = document.querySelector('.right-button img');

rightButtonImage.addEventListener('click', function() {
  // Get the hidden input field and extract the ID
  const hiddenInput = document.querySelector('#hidden-sid');
  const streakId = hiddenInput.value;

  // Increment the ID by 1 before sending the request
  const incrementedId = parseInt(streakId, 10) + 1;

  // Construct the API URL with the incremented ID
  const apiUrl = `/streak/${incrementedId}`;

  // Send the GET request to the API using Fetch API
  fetch(apiUrl)
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
      // Update the HTML with the retrieved data
      const streakTitleElement = document.querySelector('.streak-title');
      const streakDaysElement = document.querySelector('.streak-info p');
      const input = document.querySelector('#hidden-sid');
      input.value = data.id;
      streakTitleElement.textContent = data.title;
      streakDaysElement.textContent = data.days;
      
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors gracefully, e.g., display an error message to the user
    });
});


const leftButtonImage = document.querySelector('.left-button img');

leftButtonImage.addEventListener('click', function() {
  // Get the hidden input field and extract the ID
  const hiddenInput = document.querySelector('#hidden-sid');
  const streakId = hiddenInput.value;

  // Increment the ID by 1 before sending the request
  const incrementedId = parseInt(streakId, 10) - 1;

  // Construct the API URL with the incremented ID
  const apiUrl = `/streak/${incrementedId}`;

  // Send the GET request to the API using Fetch API
  fetch(apiUrl)
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
      // Update the HTML with the retrieved data
      const streakTitleElement = document.querySelector('.streak-title');
      const streakDaysElement = document.querySelector('.streak-info p');
      const input = document.querySelector('#hidden-sid');
      input.value = data.id;
      streakTitleElement.textContent = data.title;
      streakDaysElement.textContent = data.days;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors gracefully, e.g., display an error message to the user
    });
});




function updateProgressBar(percentage) {
    if (typeof percentage === 'undefined' || isNaN(percentage)) {
        console.error('Percentage is undefined or not a number');
        return;
    }

    const progressValueElement = document.querySelector('.progress-value');
    const progressLeftBar = document.querySelector('.progress-left .progress-bar');
    const progressRightBar = document.querySelector('.progress-right .progress-bar');

    const rotationValue = (percentage / 100) * 360;

    // Remove existing animation classes
    progressLeftBar.classList.remove('animate-left');
    progressRightBar.classList.remove('animate-right');

    // Trigger reflow to restart animation
    void progressLeftBar.offsetWidth;

    // Add the appropriate class for the animation
    if (percentage <= 50) {
        progressRightBar.style.transform = `rotate(${rotationValue}deg)`;
        progressLeftBar.style.transform = 'rotate(0deg)';
        progressRightBar.classList.add('animate-right');
    } else {
        progressRightBar.style.transform = 'rotate(180deg)';
        progressLeftBar.style.transform = `rotate(${rotationValue - 180}deg)`;
        progressRightBar.classList.add('animate-right');
        progressLeftBar.classList.add('animate-left');
    }

    progressValueElement.textContent = `${percentage}%`;
}

document.querySelector('.button-green').addEventListener('click', function() {
    let hiddenInput = document.getElementById('hidden-sid');
    let currentId = parseInt(hiddenInput.value);
    fetch(`/streak/${currentId}/increment_days/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Ensure you handle CSRF token
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.days !== undefined) {
            document.querySelector('.streak-info p').textContent = `${data.days}`;
        } else {
            console.error('Invalid response data:', data);
        }
    })
    .catch(error => console.error('Error:', error));
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
    var dateInput = document.querySelector('input[type="date"]');
    dateInput.addEventListener('change', function () {
        var dateValue = this.value;
        var formattedDate = new Date(dateValue).toISOString().split('T')[0];
        this.value = formattedDate;
    });
});

const taskButtons = document.querySelectorAll('.task-button');

taskButtons.forEach(button => {
  button.addEventListener('click', async () => {
    const hiddenInput = button.parentElement.querySelector('#hidden-id');
    const taskId = hiddenInput.value;
    window.location.href = `/task/update/${taskId}`;
  });
});
