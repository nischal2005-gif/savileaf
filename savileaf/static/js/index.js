// JavaScript for toggling the menu
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
const overlay = document.getElementById('overlay');
const body = document.body;

hamburger.addEventListener('click', () => {
    // navLinks.classList.toggle('active');
    body.classList.toggle('sidebar-open');
    body.classList.add('no-scroll');
});

// Hide the nav menu if clicking anywhere outside the nav and hamburger
document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
        body.classList.remove('sidebar-open');
    }
});