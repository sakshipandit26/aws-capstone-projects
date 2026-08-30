// ================================
// CONTACT BUTTON
// ================================

function showMessage() {

    const message = document.getElementById("message");

    message.textContent =
        "Thank you for visiting! ☁️ Let's build something amazing.";

}


// ================================
// NAVBAR ACTIVE LINK
// ================================

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 150;

        if (window.scrollY >= sectionTop) {

            current = section.getAttribute("id");

        }

    });


    navLinks.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {

            link.classList.add("active");

        }

    });

});


// ================================
// SIMPLE SCROLL REVEAL
// ================================

const revealElements =
    document.querySelectorAll(
        ".service-card, .project-card, .about-card"
    );


const observer = new IntersectionObserver(

    (entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    },

    {
        threshold: 0.15
    }

);


revealElements.forEach(element => {

    observer.observe(element);

});