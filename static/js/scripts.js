// static/js/scripts.js

// Function to toggle between login and register forms
function toggleForms() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const loginRadio = document.getElementById('login-radio');
    const registerRadio = document.getElementById('register-radio');

    if (loginRadio.checked) {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    } else if (registerRadio.checked) {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    }
}

// Function to handle flower (like) action
function handleFlowerClick(event) {
    const postId = event.target.getAttribute('data-post-id');
    console.log(`Flower button clicked for post ${postId}`);
    // Add your AJAX request or other logic here
}

// Function to handle comment submission
function handleCommentSubmit(event) {
    event.preventDefault();
    const postId = event.target.getAttribute('data-post-id');
    const commentText = event.target.querySelector('textarea').value;
    console.log(`Comment submitted for post ${postId}: ${commentText}`);
    // Add your AJAX request or other logic here
}

// Function to handle share action
function handleShareClick(event) {
    const postId = event.target.getAttribute('data-post-id');
    console.log(`Share button clicked for post ${postId}`);
    // Add your AJAX request or other logic here
}

// Function to handle save action
function handleSaveClick(event) {
    const postId = event.target.getAttribute('data-post-id');
    console.log(`Save button clicked for post ${postId}`);
    // Add your AJAX request or other logic here
}

// Event listener for DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for flower buttons
    document.querySelectorAll('.flower-btn').forEach(button => {
        button.addEventListener('click', handleFlowerClick);
    });

    // Add event listeners for comment forms
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', handleCommentSubmit);
    });

    // Add event listeners for share buttons
    document.querySelectorAll('.share-btn').forEach(button => {
        button.addEventListener('click', handleShareClick);
    });

    // Add event listeners for save buttons
    document.querySelectorAll('.save-btn').forEach(button => {
        button.addEventListener('click', handleSaveClick);
    });
});
