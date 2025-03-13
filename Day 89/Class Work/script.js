const check = (name, age) => 
    age >= 18 ? "${name}, you can enter" : "${name}, you cant enter";

const userName = prompt("enter your name:");
const userAge = Number(prompt("enter your age:")); 

console.log(check(userName, userAge));

const add = (a, b) => a + b;

console.log(add(6, 9)); 
console.log(add(33, 36)); 

