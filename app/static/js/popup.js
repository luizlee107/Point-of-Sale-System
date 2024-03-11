document.addEventListener('DOMContentLoaded', function () {
    const openPopupButton = document.getElementById('openPopupButton');
    const closePopupButton = document.getElementById('closePopupButton');
    const popupContainer = document.getElementById('popupContainer');
    const form = document.querySelector('.form-inline');
    const tableBody = document.querySelector('#productTable tbody'); // Assuming your table has an ID of 'productTable'

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const url = form.getAttribute('action');
        
        // Make an AJAX request
        fetch(url, {
            method: 'POST', // Change to POST
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Update the table with the filtered data
            if (data && data.products) {
                updateTable(data.products);
            } else {
                console.error('Invalid or empty response.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    openPopupButton.addEventListener('click', () => {
        popupContainer.style.display = 'block';
    });

    closePopupButton.addEventListener('click', () => {
        popupContainer.style.display = 'none';
    });

    function updateTable(products) {
        // Clear existing table rows
        tableBody.innerHTML = '';

        // Add new rows based on the filtered products
        products.forEach(product => {
            const row = tableBody.insertRow();
            // Add cells based on your Product model fields
            row.insertCell(0).textContent = product.id;
            row.insertCell(1).textContent = product.name;
            row.insertCell(2).textContent = product.group;
            row.insertCell(3).textContent = product.barcode;
            row.insertCell(4).textContent = product.price;
            // Add other cells as needed
        });
    }
});
