const updateTaskForm = document.getElementById('update-task-form');
const errorMessage = document.querySelector('.error-message');

const taskId = document.getElementById('task-id').value;
console.log(taskId)
const url = `/task/${taskId}`;

async function fetchTaskDetails() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      errorMessage.textContent = 'An error occurred fetching task details.';
    } else {
      console.log("inside ")
      const taskData = await response.json();
      console.log(taskData.title)
      document.getElementById('title').value = taskData.title;
      document.getElementById('due_date').value = taskData.due_date;
      document.getElementById('description').value = taskData.description;
      document.getElementById('progress_status').value = taskData.progress_status;
    }
  } catch (error) { 
    console.error('Error fetching task:', error);
    errorMessage.textContent = 'An error occurred.';
  }
}

// Call fetchTaskDetails to pre-fill the form on page load
fetchTaskDetails();

updateTaskForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const title = document.getElementById('title').value;
  const dueDate = document.getElementById('due_date').value;
  const description = document.getElementById('description').value;
  const progressStatus = document.getElementById('progress_status').value;

  try {
    const response = await fetch(`/task/${taskId}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Assuming you store access token in localStorage
      },
      body: JSON.stringify({
        title,
        due_date: dueDate,
        description,
        progress_status: progressStatus,
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      errorMessage.textContent = errorData.error || 'An error occurred.';
    } else {
      errorMessage.textContent = '';
    }
  } catch (error) {
    console.error('Error updating task:', error);
    errorMessage.textContent = 'An error occurred.';
  }
});


// const taskId = document.getElementById('task-id').value;
// const url = `/task/${taskId}`; // Assuming your URL pattern is similar

// try {
//   const response = await fetch(url);
//   if (!response.ok) {
//     // Handle errors fetching task details
//   } else {
//     const taskData = await response.json();
//     // Pre-fill the form with task data
//     document.getElementById('title').value = taskData.title;
//     console.log('inside')
//     // ... (fill other form elements)
//   }
// } catch (error) {
//   console.error('Error fetching task:', error);
//   errorMessage.textContent = 'An error occurred.';
// }