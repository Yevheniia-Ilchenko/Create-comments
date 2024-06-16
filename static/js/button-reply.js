document.querySelectorAll('.reply').forEach(button => {
    button.addEventListener('click', function() {
        document.getElementById('parent_id').value = this.dataset.id;
    });
});