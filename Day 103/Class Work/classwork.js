const originalObj = { a: 1, b: 2, c: 3 };
const doubledObj = manualMapObj(originalObj, value => value * 2);

console.log(doubledObj); 
console.log(originalObj); 