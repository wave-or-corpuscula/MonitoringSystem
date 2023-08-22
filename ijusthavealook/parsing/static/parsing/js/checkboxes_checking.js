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
        // newElement.textContent = fetchCompanyData(id, newElement);
        fetchCompanyData(id, newElement);
        selectedIdsBlock.appendChild(newElement);
    }

    function fetchCompanyData(observedId, newElement) {
        fetch(`/get_goods_data/?store_id=${observedId}`)
               .then(response => response.json())
               .then(data => {
                   const prices = data.prices;
                   displayStorePrices(prices, newElement);
               })
               .catch(error => console.error('Error fetching store prices:', error));
    }

    function displayStorePrices(prices, newElement) {
        if (prices.length > 0) {
            let pricesHtml = 'Цены для выбранного магазина:<br>';
            prices.forEach(price => {
                pricesHtml += `Товар ID: ${price.good_id}, Цена: ${price.price}<br>`;
            });
            newElement.innerHTML = pricesHtml;
        } else {
            newElement.textContent = 'Нет доступных цен для выбранного магазина';
        }
    }

    function removeIdBlock(id) {
        const elementToRemove = selectedIdsBlock.querySelector(`.selected-id-block[data-id="${id}"]`);
        if (elementToRemove) {
            selectedIdsBlock.removeChild(elementToRemove);
        }
    }
});
