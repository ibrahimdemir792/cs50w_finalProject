document.addEventListener('DOMContentLoaded', function() {
    const flashcard = document.getElementById('flashcard');
    const flipBtn = document.getElementById('flip-btn');
    const resultForm = document.getElementById('result-form');
    const progressBar = document.querySelector('.progress');
    const progressText = document.querySelector('.scoreboard p');
    
    let flashcards = [];
    let currentCardIndex = 0;
    let correctCount = 0;

    // Fetch flashcards data
    fetch(`/api/flashcards/${deckId}/`)
        .then(response => response.json())
        .then(data => {
            flashcards = data;
            shuffleArray(flashcards);
            showCard();
            updateProgress();
        });

    if (flipBtn && flashcard) {
        flipBtn.addEventListener('click', function() {
            flashcard.classList.toggle('flipped');
        });
    }

    if (resultForm) {
        resultForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const result = e.submitter.value;
            if (result === 'correct') correctCount++;
            currentCardIndex++;
            updateProgress();
            if (currentCardIndex < flashcards.length) {
                showCard();
            } else {
                showResults();
            }
        });
    }

    function showCard() {
        const card = flashcards[currentCardIndex];
        const frontElement = document.querySelector('.flashcard-front');
        const backElement = document.querySelector('.flashcard-back');
        if (frontElement && backElement) {
            frontElement.textContent = card.front;
            backElement.textContent = card.back;
            flashcard.classList.remove('flipped');
        } else {
            console.error('Front or back element not found');
        }
    }

    function updateProgress() {
        const progress = ((currentCardIndex + 1) / flashcards.length) * 100;
        progressBar.style.width = `${progress}%`;
        progressText.textContent = `Progress: ${correctCount} / ${currentCardIndex + 1} (${Math.round(progress)}%)`;
    }

    function showResults() {
        const accuracy = (correctCount / flashcards.length) * 100;
        const resultsHtml = `
            <h2>Study Results</h2>
            <p>Correct answers: ${correctCount}</p>
            <p>Total cards: ${flashcards.length}</p>
            <p>Accuracy: ${Math.round(accuracy)}%</p>
            <a href="/study/${deckId}/" class="btn btn-primary">Restart Deck</a>
            <a href="/study/" class="btn btn-secondary">Back to Deck List</a>
        `;
        document.querySelector('main').innerHTML = resultsHtml;
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }
});