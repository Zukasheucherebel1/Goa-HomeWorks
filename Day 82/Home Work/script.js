
let userName = prompt("Enter your name:");
let userSurname = prompt("Enter your surname:");
let userAge = prompt("Enter your age:");


let user = {
    name: userName,
    surname: userSurname,
    age: Number(userAge) 
};


console.log("User Object:", user);


user.name = "Updated Name";


console.log("Updated User Object:", user);



//რას ცვლის me.age
const me = {
    name: "Nika",
    age: 20
}

const you = me;
you.age = 25;

console.log(me.age); 



//const me = { 
  //  name: "Nika",
    //age: 20
//};
//აქ შეცდომას იმიტო აგდებს რომ const ში იგივენაირ ცვლადს ვერ ჩაწერ


const you = { ...me };  

you.age = 25;

console.log(me.age); 
console.log(you.age); 


//მათემატიკა

console.log(Math.floor(4.9)); 
console.log(Math.floor(7.2)); 
console.log(Math.floor(-2.8)); 


console.log(Math.ceil(4.1)); 
console.log(Math.ceil(7.9)); 
console.log(Math.ceil(-2.8)); 


console.log(Math.round(4.4)); 
console.log(Math.round(4.5)); 
console.log(Math.round(7.6)); 


console.log(Math.trunc(4.9)); 
console.log(Math.trunc(-7.2)); 
console.log(Math.trunc(3.99)); 


console.log(Math.random()); 
console.log(Math.random() * 10); 
console.log(Math.floor(Math.random() * 100)); 



