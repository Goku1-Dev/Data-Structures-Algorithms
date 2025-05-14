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
function GreaterOrLesser(num1,num2){
    if(num1 > num2){
        console.log(`${num1} is greater than ${num2}`);
    } else if(num1 < num2){
        console.log(`${num1} is less than ${num2}`);
    } else {
        console.log(`${num1} is equal to ${num2}`);
    }
}
let num1 = 5;
let num2 = 10;
GreaterOrLesser(num1,num2);

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

