document.addEventListener("DOMContentLoaded", function () {
    runOnScroll();
    scrollSections();
    clickLincInNavbarMobile();
});

// add scroll to top page
function scrollToTop(){
    window.scrollTo(0,0);
}

// hide mobile menu
function clickLincInNavbarMobile() {
    document.querySelectorAll('.menu_item').forEach(e => {
        e.addEventListener('click', () => {
            document.querySelector('#check').click();
        })
    })
}

window.addEventListener("scroll", runOnScroll);

// Transparency of the menu
function runOnScroll() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop >= 67) {
        document.querySelector('.header').classList.add('active');
    } else {
        document.querySelector('.header').classList.remove('active');
    };
}

// Adds page scrolling
function scrollSections() {
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('.navbar a');

    window.onscroll = () => {
        sections.forEach(sec => {
            let top = window.scrollY;
            let offset = sec.offsetTop -150;
            let height = sec.offsetHeight;
            let id = sec.getAttribute('id');

            if (top >= offset && top < offset + height ) {
                navLinks.forEach(links => {
                    links.classList.remove('active');
                    document.querySelector('.navbar a[href*=' + id + ']').classList.add('active');
                });
            };
        });
    };
}
