
function addProduct() {
    const productName = prompt("enter product name:");
    
    if (productName) {
        const newListItem = document.createElement('li');
        newListItem.textContent = productName;

        
        newListItem.addEventListener('click', function() {
            this.remove(); 
        });

        document.getElementById('productList').appendChild(newListItem);
    }
}