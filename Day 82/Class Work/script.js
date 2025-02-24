const randomNumber = Math.floor(Math.random() * 10) + 1; // 1-10 მდე გამოიტანს შემთხვევით რიცხსვს
const userGuess = parseInt(prompt("Enter a number between 1 and 10:")); // მომხმარებლის შეყვანა

if (userGuess === randomNumber) {
    console.log("You win!");
} else {
    console.log("You lose! The correct number was " + randomNumber);
}
