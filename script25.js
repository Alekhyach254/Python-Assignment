/**
 * Calculates the factorial of a non-negative integer using recursion.
 * @param {number} n The number to calculate the factorial for.
 * @returns {number | string} The factorial result or an error message.
 */
function factorial(n) {
    if (n < 0) {
        return "Error: Factorial is not defined for negative numbers.";
    }
    if (n === 0) {
        return 1;
    }

    return n * factorial(n - 1);
}


function add(a, b) { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function divide(a, b) {
    if (b === 0) {
        return "Error: Cannot divide by zero.";
    }
    return a / b;
}


function calculateFactorial() {
    const inputElement = document.getElementById('calcInput');
    const outputElement = document.getElementById('calc-output');
    

    const number = parseInt(inputElement.value);


    if (isNaN(number) || number < 0 || number !== parseFloat(inputElement.value)) {
        outputElement.textContent = "Error: Please enter a non-negative whole number.";
        return;
    }

    const result = factorial(number);
    outputElement.textContent = `${number}! = ${result}`;
}

/**

 * @param {string} operation The function name ('add', 'subtract', etc.)
 * @param {number} a First number
 * @param {number} b Second number
 */
function performOperation(operation, a, b) {
    let result;
    let operator;

    switch (operation) {
        case 'add':
            result = add(a, b);
            operator = '+';
            break;
        case 'subtract':
            result = subtract(a, b);
            operator = '-';
            break;
        case 'multiply':
            result = multiply(a, b);
            operator = '*';
            break;
        case 'divide':
            result = divide(a, b);
            operator = '/';
            break;
        default:
            result = "Invalid Operation";
    }

    document.getElementById('calc-output').textContent = `${a} ${operator} ${b} = ${result}`;
}


document.getElementById('contactForm').addEventListener('submit', function(event) {
    
    event.preventDefault(); 
    
    document.querySelectorAll('.error').forEach(span => span.textContent = '');

    let formValid = true;

    function checkEmpty(fieldId, errorId, message) {
        const field = document.getElementById(fieldId);
        const value = field.value.trim();
        if (value === '') {
            document.getElementById(errorId).textContent = message;
            field.focus(); 
            formValid = false;
            return false;
        }
        return true;
    }


    const isNameValid = checkEmpty('name', 'nameError', 'Name is required.');
    const isEmailValid = checkEmpty('email', 'emailError', 'Email is required.');
    const isMessageValid = checkEmpty('message', 'messageError', 'Message is required.');
    
 
    if (isEmailValid) {
        const email = document.getElementById('email').value.trim();
      
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/; 
        
        if (!emailPattern.test(email)) {
            document.getElementById('emailError').textContent = 'Please enter a valid email format (e.g., user@domain.com).';
            document.getElementById('email').focus();
            formValid = false;
        }
    }

    if (formValid) {
      
        alert('Form submitted successfully! (No server action coded)');
        this.reset(); 
    }
});