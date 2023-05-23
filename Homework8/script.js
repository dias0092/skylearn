const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const signupForm = document.querySelector("form.signup");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

// Slider animation Login and Signup Form
signupBtn.onclick = () => {
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
};

loginBtn.onclick = () => {
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
};

signupLink.onclick = () => {
  signupBtn.click();
  return false;
};

signupForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const emailInput = document.getElementById("signup-email-input");
  const passwordInput = document.getElementById("signup-password-input");
  const confirmPasswordInput = document.getElementById("confirm-password-input");
  const email = emailInput.value.trim();
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  // Email regex pattern
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Password length validation
  if (password.length < 8 || password.length > 20) {
    displayErrorMessage("Password should be between 8 and 20 characters.");
    return;
  }

  // Password match validation
  if (password !== confirmPassword) {
     displayErrorMessage("Passwords do not match.");
    return;
  }

  // Email validation using regex pattern
  if (!emailPattern.test(email)) {
    displayErrorMessage("Invalid email address.");
    return;
  } 

  // Redirect to the account page
  window.location.href = "account.html";

});

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const emailInput = document.getElementById("login-email-input");
  const passwordInput = document.getElementById("login-password-input");
  const email = emailInput.value.trim();
  const password = passwordInput.value;

  // Email regex pattern
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Email validation using regex pattern
  if (!emailPattern.test(email)) {
   displayErrorMessage("Invalid email address.");
    return;
  }
  if (password.length < 8 || password.length > 20) {
   displayErrorMessage("Password should be between 8 and 20 characters.");
    return;
  } 
  // Redirect to the account page
   window.location.href = "account.html";
});


const errorMessage = document.getElementById("error-message");

function displayErrorMessage(message) {
  errorMessage.textContent = message;
  errorMessage.style.display = "block";

   setTimeout(function() {
    errorMessage.style.display = 'none';
  }, 2000);
}