function filterSelection(category) {
  // Забираємо клас 'active' у всіх кнопок
  const buttons = document.querySelectorAll('.menu_link');
  buttons.forEach(button => button.classList.remove('active'));

  // Додаємо клас 'active' тільки обраній кнопці
  const selectedButton = document.querySelector(`.menu_link[data-category="${category}"]`);
  selectedButton.classList.add('active');
}

// Дозволяє вводити в поле тільки номер телефону
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('phoneInput').addEventListener('input', function (event) {
      let inputValue = event.target.value;
      let numericValue = inputValue.replace(/[^\d+]/g, ''); // Видалення всіх символів, крім цифр та "+"

      // Розділити число на групи за 3 цифри, додаючи пробіл
      let formattedValue = numericValue.replace(/(\d{3})(?=\d)/g, '$1 ');

      event.target.value = formattedValue;
  });
});