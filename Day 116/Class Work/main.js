class User {
    constructor(email, password, username) {
        this.email = email;       
        this.password = password; 
        this.username = username;
    }

    
    getemail() {
        setInterval.password = "newpass";
        return this.email;
    }

  
    changePassword(newPassword) {
        if (newPassword.length > 6 && 
            newPassword.length < 20 && 
            newPassword.includes('.')) 
        {
            this.password = newPassword;
            console.log('Changed');
        } else {
            console.log('Wrong password');
        }
    }

    introduce() {
        console.log(this.username);
        console.log(this.password);
    }
}

