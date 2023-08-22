document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.observed-checkbox');
    const selectedIdsBlock = document.getElementById('selected-ids-block');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const checkboxId = checkbox.id;
            const checkboxText = checkbox.getAttribute('name');
            if (checkbox.checked) {
                createNewIdBlock(checkboxId, checkboxText);
            } else {
                removeIdBlock(checkboxId);
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

    function removeIdBlock(id) {
        const elementToRemove = selectedIdsBlock.querySelector(`.selected-id-block[data-id="${id}"]`);
        if (elementToRemove) {
            selectedIdsBlock.removeChild(elementToRemove);
        }
    }
});
