
function submitForm(event) {
  event.preventDefault();

  const form = document.getElementById('loginForm');
  const formData = new FormData(form);
  const actionUrl = form.getAttribute('data-action-url')

  fetch(actionUrl, {
    method: 'POST',
    body: formData
  })
    .then(response => {
      if (response.redirected) {
        // Перенаправление произошло, значит успешный вход
        localStorage.setItem('showLoginSuccessMessage', 'true');
        location.reload();

      } else if (response.ok) {
        // Перенаправление не произошло, значит неверный логин или пароль
        // Вывести сообщение в форму
        var loginFailAlert = document.getElementById('loginFailAlert');
        loginFailAlert.classList.remove('visually-hidden');

      } else {
        // Обработка ошибки
        throw new Error('Network response was not ok.');
      }
    })

}

document.addEventListener('DOMContentLoaded', function() {
  if (localStorage.getItem('showLoginSuccessMessage') === 'true') {
    var myModal = new bootstrap.Modal(document.getElementById('LoginSuccessModal'), {keyboard: false});
    myModal.show();
    localStorage.setItem('showLoginSuccessMessage', 'false');
  }
});
