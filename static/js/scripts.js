function goBack() {
    // Получение URL предыдущей страницы
    var previousPageUrl = document.referrer;
    // Перенаправление на предыдущую страницу
    window.location.href = previousPageUrl;
  }