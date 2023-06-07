function goBack() {
    // Получение URL предыдущей страницы
    var previousPageUrl = document.referrer;
    // Перенаправление на предыдущую страницу
    window.location.href = previousPageUrl;
  }

document.addEventListener("DOMContentLoaded", function(){

ymaps.ready(init);
function init() {
    var suggestFullAddress = new ymaps.SuggestView('id_address');
}

});
