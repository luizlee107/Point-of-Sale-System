// popup.js
document.addEventListener('DOMContentLoaded', function () {
    const openPopupButton = document.getElementById('openPopupButton');
    const closePopupButton = document.getElementById('closePopupButton');
    const popupContainer = document.getElementById('popupContainer');

    openPopupButton.addEventListener('click', () => {
        popupContainer.style.display = 'block';
    });

    closePopupButton.addEventListener('click', () => {
        popupContainer.style.display = 'none';
    });
});