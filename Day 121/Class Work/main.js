const friendList = document.getElementById("friend-list");

const render = (users) => {
    for(const user of users) {
        friendList.innerHTML += `
            <li id="${user.id}">
                <p>${user.name}</p>
                <p>${user.username}</p>
                <p>${user.email}</p>
            </li>
        `;
    }
}

const fetchData = async (url) => {
    try {
        const response = await fetch(url);
        const users = await response.json();

        render(users)
    } catch (error) {
        console.log("error");
    }
}

fetchData("https://jsonplaceholder.typicode.com/users");