document.getElementById('add-to-cart').addEventListener('click', function(event) {
  event.preventDefault();  // Отмена отправки формы

  var form = document.getElementById('add-to-cart-form');
  var formData = new FormData(form);
  formData.append('slug', form.elements.slug.value);
  formData.append('quantity', form.elements.quantity.value);
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
      // Обработка ошибки
    });
});