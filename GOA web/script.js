document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const name = form.querySelector('input[type="text"]').value.trim();
        const email = form.querySelector('input[type="email"]').value.trim();
        const message = form.querySelector('textarea').value.trim();

        if (name === "" || email === "" || message === "") {
            alert("Please fill in all fields before submitting.");
            return;
        }

        alert("Thank you for contacting us, " + name + "! We will get back to you soon.");
        form.reset();
    });
});
