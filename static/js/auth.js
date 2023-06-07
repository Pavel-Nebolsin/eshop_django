
function submitLoginForm(event) {
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


function submitSignUpForm(event) {
  event.preventDefault();

  const form = document.getElementById('signup_form');
  const formData = new FormData(form);
  const actionUrl = form.getAttribute('data-action-url')

  fetch(actionUrl, {
  method: 'POST',
  body: formData
})
  .then(response => {
    if (response.redirected) {
      // Перенаправление произошло, значит успешная регистрация
      localStorage.setItem('showLoginSuccessMessage', 'true');
      location.reload();
    } else if (response.ok) {
      // Перенаправление не произошло, значит форма не прошла валидацию
    } else if (response.status === 400) {
      // Ответ с ошибкой валидации формы
      return response.json();
    } else {
      // Обработка других ошибок
      throw new Error('Network response was not ok.');
    }
  })
  .then(data => {
    if (data.errors) {
      // Обработка ошибок валидации формы
       Object.keys(data.errors).forEach(key => {
      const inputField = document.getElementById(`id_${key}`);
      const errorMessages = data.errors[key];
      if (inputField) {
         if(errorMessages.length > 0){
            inputField.classList.remove('is-valid');
            inputField.classList.add('is-invalid');
            } else {
            inputField.classList.remove('is-invalid');
            inputField.classList.add('is-valid');
            }
        const errorContainer = inputField.parentNode.querySelector('.invalid-feedback');
        errorContainer.textContent = errorMessages.join(', ');
      }
    });

    }
  })
  .catch(error => {
    // Обработка ошибок
    console.log(error);
  });


}

document.addEventListener('DOMContentLoaded', function() {
  if (localStorage.getItem('showLoginSuccessMessage') === 'true') {
    var loginSuccessModal = new bootstrap.Modal(document.getElementById('LoginSuccessModal'), {keyboard: false});
    loginSuccessModal.show();
    localStorage.setItem('showLoginSuccessMessage', 'false');
  }
});
