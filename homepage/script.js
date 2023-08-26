// JavaScript for interactivity

// Change background color randomly
function changeBackgroundColor() {
    const colors = ["#FF5733", "#4CAF50", "#009688", "#FFC107", "#9C27B0"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.querySelector("main").style.backgroundColor = randomColor;
}

// Attach click event to the "Change Color" button
document.querySelector("#changeColorBtn").addEventListener("click", changeBackgroundColor);

// Display alert on form submission
document.querySelector("#contactForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get the user's name and email
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;

    // Display an alert
    alert(`Thank you, ${name}! We've received your message at ${email}.`);
});
