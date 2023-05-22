// обработчик для страницы с несколькими товарами
// Получение всех кнопок с определенным классом ('add-to-cart-button')
var buttons = document.querySelectorAll('.add-to-cart-button');

// Применение обработчика событий к каждой кнопке
buttons.forEach(function(button) {
  button.addEventListener('click', function(event) {
    event.preventDefault();

    var form = button.closest('form');
    var formData = new FormData(form);
    formData.append('slug', form.elements.slug.value);
    formData.append('quantity', form.elements.quantity.value);
    formData.append('order_id', form.elements.order_id.value);

    fetch(form.action, {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Ошибка при отправке запроса');
        }
      })
      .then(data => {
        document.getElementById('cart-count').textContent = data.cart_count;
      })
      .catch(error => {
        // Обработка ошибки
      });
  });
});

// Показ сообщения

function showMessage(button) {

  var cart_button = document.getElementById('cart-button')
  var message = button.closest('.d-flex').querySelector('.message-in-item-card');

  if (message !== null) {
    cart_button.style.background = "#cfffc6"
    cart_button.style.border = "1px solid #19d51f"

    button.style.display = "none";
    message.style.display = "block";

    setTimeout(function() {
        cart_button.style.background = "none"
        cart_button.style.border = "1px solid black"
      message.style.display = "none";
      button.style.display = "block";
    }, 700);
  }
}
