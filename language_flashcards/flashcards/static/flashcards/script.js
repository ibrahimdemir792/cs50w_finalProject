document.addEventListener('DOMContentLoaded', function() {
    const flipBtn = document.getElementById('flip-btn');
    const flashcard = document.getElementById('flashcard');

    if (flipBtn && flashcard) {
        flipBtn.addEventListener('click', function() {
            flashcard.classList.toggle('flipped');
        });
    }

    // Keep the existing code for next button if you want to use it later
    const nextButton = document.querySelector('#next-button');
    if (nextButton) {
        nextButton.addEventListener('click', () => {
            // AJAX request to get next card
            fetch('/api/next-card/')
                .then(response => response.json())
                .then(data => {
                    const frontElement = document.querySelector('.flashcard-front');
                    const backElement = document.querySelector('.flashcard-back');
                    if (frontElement && backElement) {
                        frontElement.textContent = data.front;
                        backElement.textContent = data.back;
                        flashcard.classList.remove('flipped');
                    }
                });
        });
    }
});