
function sortByAge(arr, callback) {
    return arr.sort(callback);
}

const people = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 17 },
    { name: "Charlie", age: 30 }
];

console.log(sortByAge(people, (a, b) => a.age - b.age));



function applyToEach(arr, callback) {
    let result = [];
    for (let item of arr) {
        result.push(callback(item));
    }
    return result;
}

const numbers = [1, 2, 3, 4];
console.log(applyToEach(numbers, num => num * 2));



function filterAdults(arr, callback) {
    let result = [];
    for (let person of arr) {
        if (callback(person)) {
            result.push(person);
        }
    }
    return result;
}

console.log(filterAdults(people, person => person.age >= 18));



function sumAges(arr, callback, initialValue) {
    let sum = initialValue;
    for (let person of arr) {
        sum = callback(sum, person);
    }
    return sum;
}

console.log(sumAges(people, (sum, person) => sum + person.age, 0));



function findOldest(arr, callback) {
    let oldest = arr[0];
    for (let person of arr) {
        oldest = callback(oldest, person);
    }
    return oldest;
}

console.log(findOldest(people, (old, person) => (person.age > old.age ? person : old)));



function logNames(arr, callback) {
    for (let person of arr) {
        callback(person);
    }
}

logNames(people, person => console.log(person.name));



function formatPeople(arr, callback) {
    let result = [];
    for (let person of arr) {
        result.push(callback(person));
    }
    return result;
}

console.log(formatPeople(people, person => `${person.name} is ${person.age} years old.`));



function findYoungest(arr, callback) {
    let youngest = arr[0];
    for (let person of arr) {
        youngest = callback(youngest, person);
    }
    return youngest;
}

console.log(findYoungest(people, (youngest, person) => (person.age < youngest.age ? person : youngest)));



function areAllAdults(arr, callback) {
    for (let person of arr) {
        if (!callback(person)) {
            return false;
        }
    }
    return true;
}

console.log(areAllAdults(people, person => person.age >= 18));



function findMinor(arr, callback) {
    for (let person of arr) {
        if (callback(person)) {
            return person;
        }
    }
    return null;
}

console.log(findMinor(people, person => person.age < 18));



function myMap(arr, callback) {
    let result = [];
    for (let item of arr) {
        result.push(callback(item));
    }
    return result;
}

console.log(myMap([1, 2, 3], num => num * 2));



function myFilter(arr, callback) {
    let result = [];
    for (let item of arr) {
        if (callback(item)) {
            result.push(item);
        }
    }
    return result;
}

console.log(myFilter([1, 2, 3, 4], num => num > 2));



function myReduce(arr, callback, initialValue) {
    let accumulator = initialValue;
    for (let item of arr) {
        accumulator = callback(accumulator, item);
    }
    return accumulator;
}

console.log(myReduce([1, 2, 3], (acc, num) => acc + num, 0));



function myForEach(arr, callback) {
    for (let item of arr) {
        callback(item);
    }
}

myForEach([1, 2, 3], num => console.log(num));



function myFind(arr, callback) {
    for (let item of arr) {
        if (callback(item)) {
            return item;
        }
    }
    return undefined;
}

console.log(myFind([1, 2, 3, 4], num => num > 2));
