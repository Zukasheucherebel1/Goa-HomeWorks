
function manualFilter(arr, callback) {
    let filteredArr = []; 

    for (let num of arr) {
        if (callback(num)) { 
            filteredArr.push(num); 
        }
    }

    return filteredArr;
}


function isEven(num) {
    return num % 2 === 0;
}

console.log(manualFilter([1, 2, 3, 4, 5, 6, 7, 8], isEven)); // [2, 4, 6, 8]


function manualMap(arr, changer) {
    let changedArr = []; 

    for (let num of arr) {
        changedArr.push(changer(num)); 
    }

    return changedArr;
}


function double(num) {
    return num * 2;
}

console.log(manualMap([1, 2, 3, 4, 5], double)); 
