document.addEventListener('DOMContentLoaded', function() {
    const flipBtn = document.getElementById('flip-btn');
    const flashcard = document.getElementById('flashcard');

    if (flipBtn && flashcard) {
        flipBtn.addEventListener('click', function() {
            flashcard.classList.toggle('flipped');
        });
    }

    document.querySelector('#home-button').addEventListener('click', () => toggleViews('home'));
    document.querySelector('#logo').addEventListener('click', () => toggleViews('home'));
    document.querySelector('#study-button').addEventListener('click', () => toggleViews('deck-list'));
    document.querySelector('#create-deck-button').addEventListener('click', () => toggleViews('create-deck'));

    toggleViews('home');

});


function toggleViews(view) {
    if (view === 'home') {
        document.querySelector('#welcome-container').style.display = 'block';
        document.querySelector('#deck-list').style.display = 'block';

    } else if (view === 'deck-list') {
        document.querySelector('#welcome-container').style.display = 'none';
        document.querySelector('#deck-list').style.display = 'block';

    } else if (view === 'create-deck') {
        document.querySelector('#welcome-container').style.display = 'none';
        document.querySelector('#deck-list').style.display = 'none';
        document.querySelector('#create-deck').style.display = 'block';
    }
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