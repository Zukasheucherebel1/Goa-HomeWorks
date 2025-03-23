
const findEvenNumbers = (num) => {
    let evenNumbers = [];
    for (let i = 0; i <= num; i++) {
        if (i % 2 === 0) {
            evenNumbers.push(i);
        }
    }
    return evenNumbers;
};

console.log(findEvenNumbers(10)); 


function sumEvenIndexNumbers(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i += 2) {
        sum += arr[i];
    }
    return sum;
}

console.log(sumEvenIndexNumbers([10, 20, 30, 40, 50, 60])); // 10 + 30 + 50 = 90

function findLongestString(arr) {
    let longest = "";
    for (let str of arr) {
        if (str.length > longest.length) {
            longest = str;
        }
    }
    return longest;
}

console.log(findLongestString(["apple", "banana", "watermelon", "cherry"])); 


for (let i = 5; i >= 0; i--) {
    console.log(i);
}
