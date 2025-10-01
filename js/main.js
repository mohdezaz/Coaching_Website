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
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const message = document.getElementById('message').value;

            const subject = 'New Inquiry from ' + name;
            const body = `Name: ${name}%0D%0AEmail: ${email}%0D%0APhone: ${phone}%0D%0A%0D%0AMessage:%0D%0A${message}`;

            window.location.href = `mailto:clusterclasses0001@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
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
});