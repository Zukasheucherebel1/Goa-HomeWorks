const secretNumber = 7; 
let userGuess = null; 

while (userGuess !== secretNumber) {
    userGuess = parseInt(prompt("guess the number: "), 10);

    if (userGuess === secretNumber) {
        console.log("correct");
        alert("correct");
        break;
    } else {
        console.log("wrong try again.");
        alert("wrong try again.");
    }
}
