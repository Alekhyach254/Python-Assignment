function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    const taskList = document.getElementById('taskList');

    const listItem = document.createElement('li');
    listItem.textContent = taskText;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.onclick = function() {
        taskList.removeChild(listItem);
    };

   
    listItem.appendChild(removeButton);
    
   
    taskList.appendChild(listItem);


    taskInput.value = '';
}


const colorButton = document.getElementById('colorButton');
const colors = ['#f4f4f9', '#ffebee', '#e8f5e9', '#e3f2fd', '#fff3e0']; // Light colors
let currentColorIndex = 0;

colorButton.addEventListener('click', function() {
   
    currentColorIndex = (currentColorIndex + 1) % colors.length;
    document.body.style.backgroundColor = colors[currentColorIndex];
});



const dropdown = document.getElementById('messageDropdown');
const messageDisplay = document.getElementById('dropdownMessage');

const messages = {
    'message1': "You've got this! Keep going, success is just around the corner.",
    'message2': "Don't forget to take a break and stretch every hour.",
    'message3': "Did you know the official state fish of Hawaii is the Humuhumunukunukuāpuaʻa?"
};

dropdown.addEventListener('change', function() {
    const selectedValue = dropdown.value;

    messageDisplay.textContent = messages[selectedValue] || ""; 
});