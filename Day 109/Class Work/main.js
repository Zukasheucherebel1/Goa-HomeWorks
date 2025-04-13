const birthDate = new Date(1995, 4, 15, 12, 30, 0, 0); 


console.log("Complete birth date:", birthDate);


const year = birthDate.getFullYear();
const month = birthDate.getMonth(); 
const date = birthDate.getDate();
const day = birthDate.getDay(); 
const hours = birthDate.getHours();
const minutes = birthDate.getMinutes();
const seconds = birthDate.getSeconds();
const milliseconds = birthDate.getMilliseconds();

console.log("Year:", year);
console.log("Month (0-11):", month);
console.log("Date:", date);
console.log("Day of week (0-6):", day);
console.log("Hours:", hours);
console.log("Minutes:", minutes);
console.log("Seconds:", seconds);
console.log("Milliseconds:", milliseconds);