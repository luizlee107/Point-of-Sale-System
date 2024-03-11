; (function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))

    htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "dialog") {
        modal.show()
      }
    })

    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })

    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("dialog").innerHTML = ""
    })
  })()



  ; (function () {
    const toastElement = document.getElementById("toast")
    const toastBody = document.getElementById("toast-body")
    const toast = new bootstrap.Toast(toastElement, { delay: 2000 })

    htmx.on("showMessage", (e) => {
      toastBody.innerText = e.detail.value
      toast.show()
    })
  })()



  document.getElementById('filterForm').addEventListener('submit', function(event) {
    // Prevent default form submission behavior
    event.preventDefault();

    // Reload the page or redirect to the same page
    window.location.href = window.location.href;
});




document.addEventListener("DOMContentLoaded", function() {
  // Get the cash button and modal
  const cashButton = document.getElementById("cashButton");
  const cashModal = document.getElementById("cashModal");

  // Add event listener to the cash button
  cashButton.addEventListener("click", function() {
    // Calculate total money
    const totalMoney = calculateTotalMoney();

    // Update modal content with total money
    const totalMoneySpan = cashModal.querySelector("#totalMoney");
    totalMoneySpan.textContent = totalMoney;

    // Show the modal
    $(cashModal).modal("show");
  });

  // Function to calculate total money
  function calculateTotalMoney() {
    // Replace this with your actual calculation logic
    let totalMoney = 0;

    // Sum all the cart items
    document.querySelectorAll(".cart-item").forEach(function(item) {
      const subtotal = parseFloat(item.dataset.subtotal);
      totalMoney += subtotal;
    });

    return totalMoney.toFixed(2); // Adjust to the appropriate number of decimal places
  }
});



// AJAX for filtering products
$(document).ready(function() {
  $('#filterBtn').click(function() {
    var filterValue = $('#filterBarcode').val();
    $.ajax({
      url: '{% url 'pos' %}',
      type: 'GET',
      data: {
        'barcode': filterValue
      },
      success: function(data) {
        $('#productTableBody').html(data);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error("AJAX Error:", textStatus, errorThrown);
      }
    });
  });

  $('#saveBtn').click(function() {
    $('#filterForm').submit();
  });
});
