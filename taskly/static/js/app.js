// hide Django flash message after a few seconds.

// Select the element with ID "message-timer"
var message_timeout = document.getElementById("message-timer");

if (message_timeout) {
    // If the element exists, set a timeout to hide it after 5 seconds
    setTimeout(function() {
        message_timeout.style.display = "none";
    }, 5000); // 5000ms = 5 seconds
}
