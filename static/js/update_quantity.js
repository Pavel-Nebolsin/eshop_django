function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
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


