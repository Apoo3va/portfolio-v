"""
AI Software Engineering Assistant — Proposed Fix
Issue #1: Contact form does not validate email input

Add a proper reference to the email input element, attach a submit event listener to the form, and validate the email against a robust regex before allowing submission. If the test fails, prevent the default action, show an error message, and focus the input. This ensures the form cannot be submitted with an invalid email address.
"""

const form = document.querySelector('#contactForm');
const emailInput = form.querySelector('#email');
const errorMsg = form.querySelector('#emailError');

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

form.addEventListener('submit', function(e) {
  const emailValue = emailInput.value.trim();
  if (!emailPattern.test(emailValue)) {
    e.preventDefault();
    errorMsg.textContent = 'Please enter a valid email address.';
    errorMsg.style.display = 'block';
    emailInput.focus();
  } else {
    errorMsg.style.display = 'none';
  }
});
