let myArray = [1, 2, 3];
myArray.push(4);
console.log(myArray); 


function addElement(arr, element) {
    arr.push(element);
    return arr;
}

let updatedArray = addElement([10, 20, 30], 40);
console.log(updatedArray); 

 
let threeElementArray = ['apple', 'banana', 'cherry'];
threeElementArray.pop();
console.log(threeElementArray); 


threeElementArray.shift();
console.log(threeElementArray); 


let sevenElementArray = [10, 20, 30, 40, 50, 60, 70];
let middleThree = sevenElementArray.slice(2, 5);
console.log(middleThree)