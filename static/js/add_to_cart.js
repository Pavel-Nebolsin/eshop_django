document.getElementById('add-to-cart-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Отмена отправки формы

    var form = event.target;
    var formData = new FormData(form);
    formData.append('slug', form.elements.slug.value);  // Добавление слага в FormData
    formData.append('quantity', form.elements.quantity.value);  // Добавление количества в FormData
    formData.append('order_id', form.elements.order_id.value);

    fetch(form.action, {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById('cart-count').textContent = data.cart_count;
    })
    .catch(error => {

    });

  });

