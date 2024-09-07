document.addEventListener('DOMContentLoaded', () => {
    const cardElement = document.querySelector('.flashcard');
    const frontElement = document.querySelector('.front');
    const backElement = document.querySelector('.back');
    const flipButton = document.querySelector('#flip-button');
    const nextButton = document.querySelector('#next-button');

    let isFlipped = false;

    flipButton.addEventListener('click', () => {
        isFlipped = !isFlipped;
        cardElement.classList.toggle('flipped');
    });

    nextButton.addEventListener('click', () => {
        // AJAX request to get next card
        fetch('/api/next-card/')
            .then(response => response.json())
            .then(data => {
                frontElement.textContent = data.front;
                backElement.textContent = data.back;
                isFlipped = false;
                cardElement.classList.remove('flipped');
            });
    });
});