function manualForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
        callback(array[i], i, array);
    }
}

// Example usage:
const numbers = [1, 2, 3];
manualForEach(numbers, (num, index) => {
    console.log(`Element at index ${index}: ${num}`);
});


function manualMap(array, callback) {
    const newArray = [];
    for (let i = 0; i < array.length; i++) {
        newArray.push(callback(array[i], i, array));
    }
    return newArray;
}

// Example usage:
const doubled = manualMap([1, 2, 3], num => num * 2);
console.log(doubled); // Output: [2, 4, 6]

function manualFilter(array, callback) {
    const filteredArray = [];
    for (let i = 0; i < array.length; i++) {
        if (callback(array[i], i, array)) {
            filteredArray.push(array[i]);
        }
    }
    return filteredArray;
}

// Example usage:
const evens = manualFilter([1, 2, 3, 4], num => num % 2 === 0);
console.log(evens); 

