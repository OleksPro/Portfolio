function filterSelection(category) {
  // Забираємо клас 'active' у всіх кнопок
  const buttons = document.querySelectorAll('.menu_link');
  buttons.forEach(button => button.classList.remove('active'));

  // Додаємо клас 'active' тільки обраній кнопці
  const selectedButton = document.querySelector(`.menu_link[data-category="${category}"]`);
  selectedButton.classList.add('active');
}