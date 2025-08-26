                            // Home page code
                            // Registration button code

const floatRegForm = document.getElementById("regForm");
const closeWinReg = document.getElementById("closeBtnReg");
const btnReg = document.getElementById("regBtn");
btnReg.addEventListener("click", () => {
    floatRegForm.style.display = "block";
});
closeWinReg.addEventListener("click", () => {
    floatRegForm.style.display = "none";
});

                              // Login button code

const btnLog = document.getElementById("logBtn");
const floatLogForm = document.getElementById ("logForm")
const closeWinLog = document.getElementById("closeBtnLog");
btnLog.addEventListener("click", () => {
    floatLogForm.style.display = "block";
});
closeWinLog.addEventListener("click", () => {
    floatLogForm.style.display = "none";
});

                                // Submit button code for Register form

const btnSub = document.getElementById("subRegBtn");
btnSub.addEventListener("click", () => {
    floatRegForm.style.display = "block";
});

floatRegForm.addEventListener("submit", function(event){
    event.preventDefault();
    createStatusCell.innerText = "";
    
    const mail = document.getElementById("emailReg").value;
    const pass = document.getElementById("passwordReg").value;
    if (!mail || !pass){
        createStatusCell.innerText = '<p class= "error">" All fealds are required. </p>';
    }else if (pass.length < 6){
        createStatusCell.innerText = '<p class= "error"> Password must be at least 6 charachters long. </p>';
    }else {
        '<p class= "error">" You are regestered! </p>';
    }
});

const btnSub2 = document.getElementById("subLogBtn");
btnSub.addEventListener("click", () => {
    floatLogForm.style.display = "block";
});
                                // Submit button code for Login form

floatLogForm.addEventListener("submit", function(event){
    event.preventDefault();
    const statusCell = document.getElementById("emailErrorStatus");
    const mail = document.getElementById("emailLog").value;
    const pass = document.getElementById("passwordLog").value;
console.log("mail:" +mail);
console.log("pass:" +pass);
console.log("!mail" +!mail);
console.log("!pass" +!pass);
    if (!mail || !pass){
        console.log("inside !mail || !pass");
        statusCell.innerHTML = '<p class= "error"> All fields are required. </p>';
    }else if (pass.length < 6){
        statusCell.innerHTML = '<p class= "error"> Password must be at least 6 charachters long. </p>';
    }else {
        statusCell.innerHTML = '<p class= "error"> You are regestered! </p>';
    }
});

                                // Basket button cod
                                
const btnBask = document.getElementById("bask");
const closeBaskWind = document.getElementById("closeBaskPrev");
const floatBaskWind = document.getElementById("baskPrev");
btnBask.addEventListener("click", () => {
    floatBaskWind.style.display = "block";
});
closeBaskWind.addEventListener("click", () => {
    floatBaskWind.style.display = "none";
});
