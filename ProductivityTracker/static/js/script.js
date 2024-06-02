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
