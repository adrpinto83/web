
document.addEventListener('DOMContentLoaded', () => {
    // --- Scroll Animations ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    animatedElements.forEach(element => {
        observer.observe(element);
    });

    // --- Image Gallery Modal ---
    const galleryImages = document.querySelectorAll('.gallery-item img');
    const modal = document.getElementById('gallery-modal');
    const modalImg = document.getElementById('modal-image');
    const captionText = document.getElementById('modal-caption');
    const closeModal = document.querySelector('.modal .close');

    galleryImages.forEach(img => {
        img.addEventListener('click', () => {
            modal.style.display = 'block';
            modalImg.src = img.src;
            captionText.innerHTML = img.alt;
        });
    });

    if(closeModal) {
        closeModal.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    // Close modal if clicked outside the image
    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});
