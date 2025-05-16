// NOTE: Basic Level if, else, and else if statements :

// 01 : Write a program to check if a number is even or odd 
function isEven(A) {
    if (A % 2 ==0){
        console.log(`${A} is even`);
    } else {
        console.log(`${A} is odd`);
    }
}

let A = 5;
isEven(A);

// 02 : Write a program to check if a number is positive, negative, or zero
function isNumber(X){
    if(X > 0){
        console.log(`${X} is positive`);
    }
    else if(X == 0){
        console.log(`${X} is zero`);
    } 
    else {
        console.log(`${X} is negative`);
    }
}

let X = 5;
isNumber(X);

// 03 : Check if a person is eligible to vote (age >= 18)
function votingEligibility(age){
    if(age > 18){
        console.log(`${age} is eligible to vote`);
    } else if(age == 18){
        console.log(`${age} is eligible to vote`);
    } else {
        console.log(`${age} is not eligible to vote`);
    }
}

let age = 18;
votingEligibility(age);

// 04 : Find the greater or lesser numbers
function GreaterOrLesser(number1,number2){
    if(number1 > number2){
        console.log(`${number1} is greater than ${number2}`);
    } else if(number1 < number2){
        console.log(`${number1} is less than ${number2}`);
    } else {
        console.log(`${number1} is equal to ${number2}`);
    }
}
let number1 = 5;
let number2 = 10;
GreaterOrLesser(number1,number2);

// 05 : Check if a number is divisible by both 5 and 11
function divisibleByBoth(num){
    let divisibleEleven = num % 11 ==0;
    let divisibleFive = num % 5 ==0;

    if(divisibleEleven){
        console.log(`${num} is divisible by 11`);
    } else if (divisibleFive){
        console.log(`${num} is divisible by 5`);
    } else {
        console.log(`${num} is not divisible by both 5 and 11`);
    }
}

let num = 55;
divisibleByBoth(num);

// 06 : Implement a leap year checker
function leapYear(year){
    if(year % 4){
        console
    } else {
        console.log(`${year} is not a leap year`);
    }
}

let year = 2000;
leapYear(year);

// 07 : Create a grade calculator (A, B, C, D, F based on marks)
function gradeCalculator(marks){
    if(marks > 90){
        console.log(`${marks} is grade by A`);
    } else if(marks > 80){
        console.log(`${marks} is grade by B`);
    } else if(marks > 70){
        console.log(`${marks} is grade by C`);
    } else if(marks > 60){
        console.log(`${marks} is grade by D`);
    } else {
        console.log(`${marks} is grade by F`);
    }
}
let marks = 80;
gradeCalculator(marks);

// 08 : Check if three given sides form a valid triangle
function validTriangle(side1,side2,side3){
    if(side1 + side2 > side3 && side1 + side3 > side2 && side2 + side3 > side1){
        console.log(`${side1},${side2},${side3} is a valid triangle`);
    } else {
        console.log(`${side1},${side2},${side3} is not a valid triangle`);
    }
}
let side1 = 5;
let side2 = 6;
let side3 =9;
validTriangle(side1,side2,side3);

// 09 : Identify if a character is a vowel, consonant, digit, or special character
function charterType(character){
    if(character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u'){
        console.log(`${character} is a vowel`);
    } else if(character >= '0' && character <= '9'){
        console.log(`${character} is a digit`);
    } else {
        console.log(`${character} is a special character`);
    }
}

let character = 'a';
charterType(character);

// 10 : Build a simple calculator (+, -, *, /)
function calculator(num1,num2,num3){
    if(num3 == '+'){
        console.log(`${num1} + ${num2} = ${num1 + num2}`);
    } else if(num3 == '-'){
        console.log(`${num1} -${num2} = ${num1 - num2}`);
    } else if(num3 == '*'){
        console.log(`${num1 * num2} = ${num1 * num2}`);
    } else{
        console.log(`${num1} / ${num2} = ${num1 / num2}`);
    }
}

let num1 = 5;
let num2 = 10;
let num3 = '+';
calculator(num1,num2,num3);

// ___________________________________________________________________________________________________

function simpleCalculator(num1, num2) {
    console.log(
        '\n- subraction,\n- addition,\n- multiplication,\n- division\n'
    );
    let operation = getUserInput();

    function subraction(num1, num2) {
        console.log(num1 - num2);
    }
    function sum(num1, num2) {
        console.log(num1 + num2);
    }
    function division(num1, num2) {
        console.log(num1 / num2);
    }
    function multiplication(num1, num2) {
        console.log(num1 * num2);
    }

    if (operation == 'addition') {
        sum(num1, num2);
    } else if (operation == 'subraction') {
        subraction(num1, num2);
    } else if (operation == 'division') {
        division(num1, num2);
    } else if (operation == 'multiplication') {
        multiplication(num1, num2);
    }
}

simpleCalculator(5, 10);


// NOTE: Advanced Level
// 11 : Find the largest of three numbers
function largestOfThree(arr){
    let largest = arr[0];
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > largest){
            largest = arr[i];
        }
    }
    console.log(`${largest} is the largest number`);
}

let arr = [5,10,15];
largestOfThree(arr);

// 12 : Implement a profit or loss calculator
function ProfitOrLoss(investment, earnings){
    investment = Number(investment);
    earnings = Number(earnings);

    if(earnings > investment){
        console.log(`You made a profit of ${earnings - investment}`);
    } else if(earnings < investment){
        console.log(`You made a loss of ${investment - earnings}`);
    } else {
        console.log(`You made no profit or loss`);
    }
}
let investment = 1000;
let earnings = 1200;
ProfitOrLoss(investment,earnings);

// 13 : Write an electricity bill calculator with tiered pricing
function electricityBillCalculator(units){
    if(units <= 100){
        console.log(`Your electricity bill is ${units * 0.5}`);
    } else if(units <= 200){
        console.log(`Your electricity bill is ${100 * 0.5 + (units - 100) * 0.75}`);
    } else {
        console.log(`Your electricity bill is ${100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2}`);
    }
}

let units = 300;
electricityBillCalculator(units);

// 14 : Determine the type of triangle (Equilateral, Isosceles, Scalene)
function typeOfTriangle(sideA,sideB,sideC){
    if(sideA == sideB && sideB == sideC){
        console.log(`${sideA},${sideB},${sideC} is an equilateral triangle`);
    } else if(sideA == sideB || sideB == sideC || sideA == sideC){
        console.log(`${sideA},${sideB},${sideC} is an isosceles triangle`);
    } else {
        console.log(`${sideA},${sideB},${sideC} is a scalene triangle`);
    }
}

let sideA = 5;
let sideB = 5;
let sideC = 5;
typeOfTriangle(sideA,sideB,sideC);

// 15 : Map numbers 1-7 to corresponding days of the week
function dayOfTheWeek(day){
    switch(day){
        case 1:
            console.log(`Day ${day} is Monday`);
            break;
        case 2:
            console.log(`Day ${day} is Tuesday`);
            break;
        case 3:
            console.log(`Day ${day} is Wednesday`);
            break;
        case 4:
            console.log(`Day ${day} is Thursday`);
            break;
        case 5:
            console.log(`Day ${day} is Friday`);
            break;
        case 6:
            console.log(`Day ${day} is Saturday`);
            break;
        case 7:
            console.log(`Day ${day} is Sunday`);
            break;
        default:
            console.log(`Invalid day`);
    }
}
let day = 5;
dayOfTheWeek(day);