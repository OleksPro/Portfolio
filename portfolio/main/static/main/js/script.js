document.addEventListener("DOMContentLoaded", function () {
    var menuItems = document.querySelectorAll('.menu_item');
    
    menuItems.forEach(function (menuItem) {
        menuItem.addEventListener('click', function (event) {
            event.preventDefault();
            var target = event.currentTarget.getAttribute('data-target');
            scrollToHandler(target);
        });
    });
});

function scrollToHandler(elementId) {
    var element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
            inline: 'start'
        });
    } else {
        console.error("Елемент з ідентифікатором " + elementId + " не знайдено.");
    }
}
