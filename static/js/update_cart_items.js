
function reduceCartCount() {

  var cartCountElement = document.getElementById('cart-count');
  if (cartCountElement) {
    var currentCount = parseInt(cartCountElement.textContent);
        if(currentCount > 0){
      cartCountElement.textContent = currentCount - 1;
        }
  }


}
function updateOrderTotalAmount() {
  var ItemsTotal = document.querySelectorAll('.total-price');
  var totalAmount = 0;

ItemsTotal.forEach(function(item) {
  var totalPrice = parseInt(item.textContent);
  totalAmount += totalPrice;
});

  var cartTotalAmountElement = document.getElementById('order-total-amount');
  cartTotalAmountElement.textContent = totalAmount;

      if(totalAmount <= 0){
        disablePayButton();
    }
}

function updateQuantity(itemID, change, url) {
  var inputField = document.querySelector(`input[name="quantity"][data-item="${itemID}"]`);
  var newQuantity = parseInt(inputField.value) + change;
  if (newQuantity >= 1) {
    inputField.value = newQuantity;
    var formData = new FormData();
    formData.append('item_id', itemID);
    formData.append('quantity', newQuantity);

    var csrfToken = getCookie('csrftoken'); // Получение CSRF-токена

    fetch(url, {
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
            totalPriceElement.textContent = updatedTotalPrice;
          }
        // Обновление общей суммы корзины
            updateOrderTotalAmount()

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
    var actionUrl = button.getAttribute('data-action-url');
    var is_cart = button.getAttribute('data-is-cart');
    deleteItem(itemId,actionUrl,is_cart);
  });
});

// Функция для отправки запроса на удаление товара
function deleteItem(itemId,actionUrl,is_cart) {
    var csrfToken = getCookie('csrftoken'); // Получение CSRF-токена
  fetch( actionUrl, {
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
        // Уменьшение цифры количества товаров в корзине в навбаре
            if(is_cart==='true'){
            reduceCartCount()
            }
        // Обновление общей суммы корзины
            updateOrderTotalAmount()

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