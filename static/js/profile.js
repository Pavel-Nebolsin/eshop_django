// инициализация строки адреса с подсказками от Яндекс-карт
document.addEventListener("DOMContentLoaded", function(){

ymaps.ready(init);
function init() {
    var suggestFullAddress = new ymaps.SuggestView('id_address');
}

});

function editForm(){
var editButton = document.getElementById('editProfileButton');
var saveButton = document.getElementById('saveProfileButton');
var formFields = document.querySelectorAll('input[disabled], textarea[disabled]');

// Блокируем кнопки отправки подтверждений имэйла и телефона
var emailConfirmButton = document.getElementById('emailConfirmButton');
var phoneNumberConfirmButton = document.getElementById('phoneNumberConfirmButton');
emailConfirmButton.disabled = true;
phoneNumberConfirmButton.disabled = true;

  // Удаляем атрибут disabled у всех полей формы
  formFields.forEach(function(field) {
    field.removeAttribute('disabled');
  });

  // Скрываем кнопку Изменить и показываем кнопку Сохранить
  editButton.style.display = 'none';
  saveButton.style.display = 'block';

}

// Сохранение положения прокрутки страницы при отправке формы
function saveScrollPosition() {
  sessionStorage.setItem('scrollPosition', window.scrollY);
}

// отправка подтверждения имейла
var emailConfirmButton = document.getElementById('emailConfirmButton');

emailConfirmButton.addEventListener('click', function(event){
emailConfirmButton.disabled = true;
var span = emailConfirmButton.closest('div').querySelector('span');
span.textContent = "Письмо отправлено";
var actionUrl = this.getAttribute('data-action-url');
var csrfToken = getCookie('csrftoken'); // Получение CSRF-токена

fetch(actionUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({}),
})
    .then(response => {
        if (response.ok) {
            console.log('Запрос успешно отправлен');
            return response.json();
        } else {
            console.log('Произошла ошибка при отправке запроса');
            throw new Error('Error');
        }
    })
    .then(data => {
        // Обработка ответа от сервера
    })
    .catch(error => {
        console.log(error)
    });

});


// Восстановление положения прокрутки страницы после обновления
function restoreScrollPosition() {
  var scrollPosition = sessionStorage.getItem('scrollPosition');
  if (scrollPosition) {
    window.scrollTo(0, scrollPosition);
    sessionStorage.removeItem('scrollPosition');
  }
}

// Обработчик события отправки формы
function handleFormSubmit() {
  saveScrollPosition();
}

// Восстановление положения прокрутки при загрузке страницы
document.addEventListener('DOMContentLoaded', restoreScrollPosition);

// Привязка обработчика события отправки формы
var form = document.querySelector('#profileForm');
form.addEventListener('submit', handleFormSubmit);


document.addEventListener('DOMContentLoaded', function() {
  if (localStorage.getItem('showEmailConfirmedMessage') === 'true') {
    var Modal = new bootstrap.Modal(document.getElementById('EmailConfirmedModal'), {keyboard: false});
    Modal.show();
    localStorage.setItem('showEmailConfirmedMessage', 'false');
  }
});
