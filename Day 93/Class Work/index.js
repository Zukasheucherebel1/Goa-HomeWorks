 // N1
 numbers.push(10, 25, 37, 42, 59);
       console.log(numbers);

      
      // N2
      let cities = ["Tbilisi", "Paris"];
      cities.push("tajikistnan", "avganistan");
      console.log(cities);
      
      
      // N3

      function addToArray(xxi, jaja) {
        xxi.push(jaja); 
        return xxi; }
    
    let numbers = [20, 8, 6]; 
    console.log(addToArray(numbers, 7)); 
    console.log(addToArray(numbers, 9));

    // N4
    let chvenipatartadzmebi = ["dog", "cat",]; 

    chvenipatartadzmebi.pop(); 
    
    console.log(chvenipatartadzmebi); 

    // N5
    let weekdays = ["Tuesday", "Wednesday", "Thursday"];


weekdays.unshift("Monday");

console.log(weekdays); 


function addToStart(arr, value) {
    arr.unshift(value);
    return arr;
}
let newWeekdays = addToStart(weekdays, "Sunday");

console.log(newWeekdays); 


//N6
let drinks = ["kofe", "chai", "sandoras wveni", "kokakola"];


drinks.shift();
drinks.shift();

console.log(drinks); 

//N7
let words = ["baro", "kamanda", "JavaScript", "magra", "asworebs"];


let newWords = words.slice(2, 4);

console.log(newWords); 
console.log(words); 