// global variables
const x =100;
const y =50;
let myValue;
let myValue2;

function loadValues() {
    document.getElementById("xValue").innerHTML = x;
    document.getElementById("yValue").innerHTML = y;
}

// Box 1 Arithmetic Operators
function add() {
    myValue = x + y;
    document.getElementById("displayresult").innerHTML = myValue
}


function subtract() {
    myValue = x - y;
    document.getElementById("displayresult").innerHTML = myValue
}

function multiply() {
    myValue = x * y;
    document.getElementById("displayresult").innerHTML = myValue
}

function divide() {
    myValue = x / y;
    document.getElementById("displayresult").innerHTML = myValue
}

function increment() {
    myValue = x;
    myValue = ++myValue;
    document.getElementById("displayresult").innerHTML = myValue
}

function decrement() {
    myValue = y;
    myValue = --myValue;
    document.getElementById("displayresult").innerHTML = myValue
}

//Box 2 - More Math
function calcRectangle() {
    let length = prompt("Enter Length:");
    length = parseFloat(length);

    let width = prompt("Enter Width:")
    width = parseFloat(width);

    let areaIs = length * width;
    let perimiterIs = (2 * length) + (2 * width);

    document.getElementById("areaResult").textContent = areaIs;
    document.getElementById("perimeterResult").textContent = perimiterIs;
}   

// box 3 - average test scores
/* comment for multiple lines */

function avgCalc() {
    let entry;
    let average;
    let total = 0;

    entry = prompt("Enter test score #1");
    let score1 = parseInt(entry);
    total += score1;

    entry = prompt("Enter test score #2");
    let score2 = parseInt(entry);
    total += score2;

    entry = prompt("Enter test score #3");
    let score3 = parseInt(entry);
    total += score3;

//calculate the average
    average = parseInt(total/3);

    document.getElementById("avgResult").innerHTML = average
}

// Box 4 - Comparison Operators
function numGuess() {
    let entry = prompt("Enter a number between 1 and 100");
    let luckyNum = 57;

    entry = parseInt(entry);

    if(entry == luckyNum) {
        alert("Congratulations! That's the LUCKY number!");
    } else { 
        alert("Sorry, that's not the lucky number. \n" + "Please try again");
    }
}