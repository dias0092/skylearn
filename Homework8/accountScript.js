document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the form element and add a submit event listener
    var form = document.getElementById('top-up-form');
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
  
      // Get the selected option and the entered amount
      var select = document.getElementById('inputGroupSelect01');
      var amountInput = document.getElementById('amount-input');
      var selectedOption = select.options[select.selectedIndex].text;
      var amount = parseFloat(amountInput.value);
  
      // Update the transaction history table
      var tableBody = document.getElementById('transaction-history-body');
      var row = tableBody.insertRow(0); // Insert the row at index 0 to add it at the beginning
      var dateCell = row.insertCell(0);
      var descriptionCell = row.insertCell(1);
      var amountCell = row.insertCell(2);
      var balanceCell = row.insertCell(3);
  
      var dateText = document.createElement('strong');
      dateText.textContent = getCurrentDate();
      dateCell.appendChild(dateText);
      descriptionCell.textContent = selectedOption;
      amountCell.textContent = (amount >= 0 ? '+' : '') + amount + '₸';
  
      // Calculate the new balance
      var balance = parseFloat(document.getElementById('balance').textContent);
      var newBalance = balance + amount;
      balanceCell.textContent = newBalance + '₸';
  
      // Update the balance on the page
      document.getElementById('balance').textContent = newBalance;
  
      // Reset the form fields
      select.selectedIndex = 0;
      amountInput.value = '';
    });
  });
  
  // Function to get the current date in the format "DD/MM/YYYY"
  function getCurrentDate() {
    var today = new Date();
    var day = String(today.getDate()).padStart(2, '0');
    var month = String(today.getMonth() + 1).padStart(2, '0');
    var year = today.getFullYear();
    return day + '/' + month + '/' + year;
  }