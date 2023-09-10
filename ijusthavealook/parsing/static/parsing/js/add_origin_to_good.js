document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.void-goods-item');
    let add_goods_ids = [];
    document.getElementById('add-to-good').addEventListener('click', function () {
        add_goods_ids = [];
        var good_id = this.getAttribute('data-good-id');
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                checkbox.checked = true;
                const name = checkbox.getAttribute('name');
                add_goods_ids.push(name);
            }
        });
        
        // Выполняем fetch-запрос
        fetch(`/add_origin_to_good/?origin_id=${good_id}&correspond_good_ids=${add_goods_ids.join(',')}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                // Если запрос успешен, выполняем перенаправление
                window.location.href = `/goods/${good_id}`;
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Дополнительная обработка ошибки, если необходимо
            });
    });
});
