// Add event listeners to all delete buttons
document.querySelectorAll('.deleteButton').forEach(function(button) {
    button.addEventListener('click', function() {
        var cardId = this.getAttribute('data-card-id');
        if (confirm("Are you sure you want to delete?")) {
            // Perform AJAX request to delete the card
            fetch('/delete_card/' + cardId, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    // Remove the card from the list
                    this.closest('li').remove();
                    alert("Deleted successfully!");
                } else {
                    alert("Error deleting. Please try again.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Error deleting. Please try again.");
            });
        }
    });
});