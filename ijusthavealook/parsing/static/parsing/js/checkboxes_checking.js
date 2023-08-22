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

    document.getElementById('check-all-checkboxes').addEventListener('click', function () {
        checkboxes.forEach(checkbox => {
            if (!checkbox.checked) {
                checkbox.checked = true;
                const checkboxText = checkbox.getAttribute('name');
                createNewIdBlock(checkbox.id, checkboxText);
            }
        });
    });

    document.getElementById('clear-checkboxes').addEventListener('click', function () {
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                checkbox.checked = false;
                removeIdBlock(checkbox.id);
            }
        });
    });

    function createNewIdBlock(id, checkboxText) {
        const newElement = document.createElement('div');
        newElement.className = 'selected-id-block';
        newElement.setAttribute('data-id', id);
        fetchCompanyData(id, newElement, checkboxText);
        selectedIdsBlock.appendChild(newElement);
    }

    function fetchCompanyData(observedId, newElement, checkboxText) {
        fetch(`/get_goods_data/?store_id=${observedId}`)
               .then(response => response.json())
               .then(data => {
                    newElement.innerHTML = generatePricesHtml(data.prices, checkboxText);
               })
               .catch(error => console.error('Error fetching store prices:', error));
    }

    function generatePricesHtml(prices, checkboxText) {
        let pricesHtml = '<p>' + checkboxText + ':</p><ul>';
        prices.forEach(price => {
            pricesHtml += `<li>Товар ID: ${price.good_id}, Цена: ${price.price}</li>`;
        });
        pricesHtml += '</ul>';
        return pricesHtml;
    }

    function removeIdBlock(id) {
        const elementToRemove = selectedIdsBlock.querySelector(`.selected-id-block[data-id="${id}"]`);
        if (elementToRemove) {
            selectedIdsBlock.removeChild(elementToRemove);
        }
    }
});

