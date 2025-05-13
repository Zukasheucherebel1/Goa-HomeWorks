function copyObj(sourceObj, copyObj) {
    for (let key in copyObj) {
        sourceObj[key] = copyObj[key];
    }
    return sourceObj;
}

// Testing the function
const original = { a: 1, b: 2 };
const toCopy = { b: 3, c: 4 };
const result = copyObj(original, toCopy);
console.log(result); 