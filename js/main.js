document.addEventListener("DOMContentLoaded", function() {
    // Accordion Logic
    var acc = document.getElementsByClassName("accordion");
    for (var i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }

    // Contact Form Logic
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(event) {
            event.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const message = document.getElementById('message').value;

            const response = await fetch('http://127.0.0.1:5000/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, phone, message }),
            });

            const result = await response.json();
            if (response.ok) {
                alert(result.message);
                contactForm.reset();
            } else {
                alert('Error: ' + JSON.stringify(result.errors));
            }
        });
    }

    // Scroll Animation Logic
    const fadeInElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    fadeInElements.forEach(element => {
        observer.observe(element);
    });

    // Gallery Lightbox Logic
    const modal = document.getElementById("lightbox-modal");
    if (modal) {
        const modalImg = document.getElementById("lightbox-img");
        const galleryImages = document.querySelectorAll(".gallery-img");
        const closeBtn = document.querySelector(".close-lightbox");

        galleryImages.forEach(img => {
            img.addEventListener("click", function() {
                modal.style.display = "block";
                modalImg.src = this.src;
            });
        });

        closeBtn.addEventListener("click", function() {
            modal.style.display = "none";
        });

        window.addEventListener("click", function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        });
    }

    // Mobile Navigation Logic
    const hamburger = document.querySelector('.hamburger-menu');
    const mobileNav = document.getElementById('mobile-nav');
    const closeBtn = document.querySelector('.close-btn');

    if (hamburger && mobileNav && closeBtn) {
        hamburger.addEventListener('click', function() {
            mobileNav.style.width = '100%';
            document.body.classList.add('mobile-nav-open');
        });

        closeBtn.addEventListener('click', function() {
            mobileNav.style.width = '0';
            document.body.classList.remove('mobile-nav-open');
        });
    }

    // Login/Signup Popup Logic
    const loginPopup = document.getElementById('login-popup');
    const closePopupBtn = document.querySelector('.close-popup-btn');
    const loginView = document.getElementById('login-view');
    const signupView = document.getElementById('signup-view');
    const showSignupBtn = document.getElementById('show-signup');
    const showLoginBtn = document.getElementById('show-login');
    const signupForm = document.getElementById('signup-form');
    const loginForm = document.getElementById('login-form');

    if (loginPopup && closePopupBtn) {
        // Show popup after 30 seconds
        setTimeout(() => {
            if (loginPopup.style.display !== 'flex') {
                loginPopup.style.display = 'flex';
            }
        }, 30000);

        // Close popup when the close button is clicked
        closePopupBtn.addEventListener('click', () => {
            loginPopup.style.display = 'none';
        });

        // Close popup when clicking outside the content
        window.addEventListener('click', (event) => {
            if (event.target == loginPopup) {
                loginPopup.style.display = 'none';
            }
        });

        // Toggle to signup view
        showSignupBtn.addEventListener('click', (e) => {
            e.preventDefault();
            loginView.style.display = 'none';
            signupView.style.display = 'block';
        });

        // Toggle to login view
        showLoginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            signupView.style.display = 'none';
            loginView.style.display = 'block';
        });

        // Handle Signup Form Submission
        signupForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('signup-username').value;
            const email = document.getElementById('signup-email').value;
            const password = document.getElementById('signup-password').value;
            const confirmPassword = document.getElementById('signup-confirm-password').value;

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return;
            }

            const response = await fetch('http://127.0.0.1:5000/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, email, password, confirm_password: confirmPassword })
            });

            const result = await response.json();
            if (response.ok) {
                alert(result.message);
                showLoginBtn.click(); // Switch to login view
            } else {
                alert('Error: ' + JSON.stringify(result.errors));
            }
        });

        // Handle Login Form Submission
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('login-email').value;
            const password = document.getElementById('login-password').value;

            const response = await fetch('http://127.0.0.1:5000/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const result = await response.json();
            if (response.ok) {
                alert(result.message);
                loginPopup.style.display = 'none';
                // Here you would typically save a token and update the UI
            } else {
                alert('Error: ' + result.message);
            }
        });
    }
});