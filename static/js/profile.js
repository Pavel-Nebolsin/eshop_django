
function editForm(){
var editButton = document.getElementById('editProfileButton');
var saveButton = document.getElementById('saveProfileButton');
var formFields = document.querySelectorAll('input[disabled], textarea[disabled]');

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
