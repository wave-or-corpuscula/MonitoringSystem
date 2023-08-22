document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.observed-checkbox');
    const selectedIdsBlock = document.getElementById('selected-ids-block');

    document.getElementById('check-all-checkboxes').addEventListener('click', function () {
        checkboxes.forEach(checkbox => {
            if (!checkbox.checked) {
                checkbox.checked = true;
                const checkboxText = checkbox.getAttribute('name');
                createNewIdBlock(checkbox.id, checkboxText);
            }
        });
    });

    function createNewIdBlock(id, text) {
        const newElement = document.createElement('div');
        newElement.className = 'selected-id-block';
        newElement.setAttribute('data-id', id);
        newElement.textContent = `${text}`;
        selectedIdsBlock.appendChild(newElement);
    }
});