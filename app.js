// Display Mobile Menu
const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

const mobileMenu = () => {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobileMenu);

// Navbar stuff
const navLogo = document.querySelector('#navbar__logo')

// Show active menu when scrolling
const highlightMenu = () => {
    const menuHighlight = document.querySelector('.highlight')
    const homeMenu = document.querySelector('#home-page')
    const aboutMenu = document.querySelector('#about-page')
    const servicesMenu = document.querySelector('#services-page')
    // Get current scroll height of page
    let scrollPos = window.scrollY

    // adds 'highlight class to menu items
    if (window.innerWidth > 960) {// only show on desktop view
        if (scrollPos < 600) { 
            homeMenu.classList.add('highlight')
            aboutMenu.classList.remove('highlight')
            return
        }
        else if (scrollPos < 1400) {
            homeMenu.classList.remove('highlight')
            aboutMenu.classList.add('highlight')
            servicesMenu.classList.remove('highlight')
            return
        }
        else if (scrollPos < 2345) {
            aboutMenu.classList.remove('highlight')
            servicesMenu.classList.add('highlight')
            return
        }
    }
    if ((menuHighlight && window.innerWidth < 960 && scrollPos < 600) || menuHighlight) {
        menuHighlight.classList.remove('highlight')
    }
}
window.addEventListener('scroll', highlightMenu)
window.addEventListener('click', highlightMenu)

// Close mobile menu after clicking menu item
const hideMobileMenu = () => {
    const menuBars = document.querySelector('.is-active')
    if(window.innerWidth <= 768 && menuBars) {
        menu.classList.toggle('is-active')
        menuLinks.classList.remove('active')
    }
}

menuLinks.addEventListener('click', hideMobileMenu)
navLogo.addEventListener('click', hideMobileMenu)