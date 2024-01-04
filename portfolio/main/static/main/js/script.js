document.addEventListener("DOMContentLoaded", function () {
    runOnScroll();
    scrollSections();
});

window.addEventListener("scroll", runOnScroll);

// Прозорість навбара
function runOnScroll() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop >= 67) {
        document.querySelector('.header').classList.add('active');
    } else {
        document.querySelector('.header').classList.remove('active');
    };
}

function scrollSections() {
    // Додає скролл сторінки
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('.header_menu a');

    window.onscroll = () => {
        sections.forEach(sec => {
            let top = window.scrollY;
            let offset = sec.offsetTop -150;
            let height = sec.offsetHeight;
            let id = sec.getAttribute('id');

            if (top >= offset && top < offset + height ) {
                navLinks.forEach(links => {
                    links.classList.remove('active');
                    document.querySelector('.header_menu a[href*=' + id + ']').classList.add('active');
                });
            };
        });
    };
}