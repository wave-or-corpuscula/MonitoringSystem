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

        // console.log(`/add_origin_to_good/?origin_id=${good_id}&correspond_good_ids=${add_goods_ids.join(',')}`);
        fetch(`/add_origin_to_good/?origin_id=${good_id}&correspond_good_ids=${add_goods_ids.join(',')}`)
            //    .then(response => response.json())
            //    .then(data => {
                    
            //    })
            //    .catch(error => console.error('Error fetching store prices:', error));

    });
});
