const numbers = [1,2,3,4,5,6,7,8,9,10];

numbers.forEach(curValue => {
    curValue % 2 === 0 ? console.log("Number is Even") : 
    console.log("Number is Odd");
});




const alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

const symbols = alphabet.map((curValue, index) => `${curValue} - ${index + 1}`);

console.log(symbols);


const people = [
    { name: "Alice", age: 30, occupation: "Engineer" },
    { name: "Bob", age: 25, occupation: "Designer" },
    { name: "Charlie", age: 35, occupation: "Teacher" },
    { name: "David", age: 28, occupation: "Developer" },
    { name: "Eva", age: 32, occupation: "Manager" }
  ];
  
  
  const filteredPeople = people.filter(person => person.age >= 30);
  
  console.log(filteredPeople);
