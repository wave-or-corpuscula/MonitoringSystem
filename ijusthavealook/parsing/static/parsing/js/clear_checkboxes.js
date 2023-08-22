document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.observed-checkbox');
    const selectedIdsBlock = document.getElementById('selected-ids-block');

    document.getElementById('clear-checkboxes').addEventListener('click', function () {
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                checkbox.checked = false;
                removeIdBlock(checkbox.id);
            }
        });
    });

    function removeIdBlock(id) {
        const elementToRemove = selectedIdsBlock.querySelector(`.selected-id-block[data-id="${id}"]`);
        if (elementToRemove) {
            selectedIdsBlock.removeChild(elementToRemove);
        }
    }
});