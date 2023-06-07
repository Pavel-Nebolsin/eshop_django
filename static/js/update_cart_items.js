
function reduceCartCount() {

  var cartCountElement = document.getElementById('cart-count');
  if (cartCountElement) {
    var currentCount = parseInt(cartCountElement.textContent);
        if(currentCount > 0){
      cartCountElement.textContent = currentCount - 1;
        }
  }


}
function updateCartTotalAmount() {
  var cartItems = document.querySelectorAll('.cart-item');
  var totalAmount = 0;

  cartItems.forEach(function(item) {
    var totalPriceElement = item.querySelector('.total-price');
    var totalPrice = parseInt(totalPriceElement.textContent);
    totalAmount += totalPrice;
  });

  var cartTotalAmountElement = document.getElementById('cart-total-amount');
  cartTotalAmountElement.textContent = totalAmount + ' р.';

      if(totalAmount <= 0){
        disablePayButton();
    }
}

function updateQuantity(itemID, change) {
  var inputField = document.querySelector(`input[name="quantity"][data-item="${itemID}"]`);
  var newQuantity = parseInt(inputField.value) + change;
  if (newQuantity >= 1) {
    inputField.value = newQuantity;
    var formData = new FormData();
    formData.append('item_id', itemID);
    formData.append('quantity', newQuantity);

    var csrfToken = getCookie('csrftoken'); // Получение CSRF-токена

    fetch('update-quantity/', {
      method: 'POST',
      headers: {
      'X-CSRFToken': csrfToken
        },
      body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Обновление значения total_price продукта на странице
          var itemID = data.item_id;
          var updatedTotalPrice = data.total_price;

          var totalPriceElement = document.querySelector(`#total-price-${itemID}`);
          if (totalPriceElement) {
            totalPriceElement.textContent = updatedTotalPrice + ' р.';
          }
        // Обновление общей суммы корзины
            updateCartTotalAmount()

    })
    .catch(error => {
      // Обработка ошибок, если необходимо
    });
  }
}

// УДАЛЕНИЕ ПРОДУКТА ИЗ КОРЗИНЫ
// Получение всех кнопок удаления
var deleteButtons = document.querySelectorAll('.bi-trash');

// Применение обработчика событий к каждой кнопке удаления
deleteButtons.forEach(function(button) {
  button.addEventListener('click', function(event) {
    event.preventDefault();

    var itemId = button.getAttribute('data-item-id');
    deleteItem(itemId);
  });
});

// Функция для отправки запроса на удаление товара
function deleteItem(itemId) {
    var csrfToken = getCookie('csrftoken'); // Получение CSRF-токена
  fetch('delete-item/' + itemId, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  })
    .then(response => {
      if (response.ok) {
        // Успешное удаление
        // Удалить соотвествующий элемент DOM для удаленного товара
      var cartItem = document.querySelector('.cart-item[data-item="' + itemId + '"]');
      cartItem.remove();
        // Обновление общей суммы корзины
            updateCartTotalAmount()
        // Уменьшение цифры количества товаров в корзине в навбаре
            reduceCartCount()

      } else {
        throw new Error('Ошибка при удалении товара');
      }
    })
    .catch(error => {
      // Обработка ошибки
    });
}

function disablePayButton(){
var cartToPayButton = document.getElementById('cart-to-pay');
        cartToPayButton.classList.add('disabled');
        cartToPayButton.classList.add('not-allowed')
        cartToPayButton.tabIndex = "-1"

}