document.addEventListener('DOMContentLoaded', function() {
    const flipBtn = document.getElementById('flip-btn');
    const flashcard = document.getElementById('flashcard');
    let currentFlashcard = null; // Track the current flashcard

    if (flipBtn && flashcard) {
        flipBtn.addEventListener('click', function() {
            flashcard.classList.toggle('flipped');
        });
    }

    document.getElementById('next-btn').addEventListener('click', showNextCard);

    // Check answer while user is typing
    document.getElementById('answer').addEventListener('input', checkAnswer);

    if (document.title === 'Study Session') {
        const deckId = document.body.dataset.deckId;
        fetch(`/get_flashcards/${deckId}/`)
            .then(response => response.json())
            .then(data => {
                flashcardsArray = data; // Assign the fetched data to the global flashcardsArray
                console.log('Flashcards fetched into global flashcardsArray:', flashcardsArray);
                showNextCard();
            })
            .catch(error => {
                console.error('Error fetching flashcards:', error);
            });
    }
});

let flashcardsArray = []; // Declare flashcards in the global scope

function showNextCard() {
    if (flashcardsArray.length === 0) {
        console.log('No flashcards available');
        document.getElementById('flashcard-front').textContent = "No more cards";
        document.getElementById('flashcard-back').textContent = "";
        return;
    }

    // Pick a random flashcard but don't remove it
    const randomIndex = Math.floor(Math.random() * flashcardsArray.length);
    currentFlashcard = flashcardsArray[randomIndex]; // Save the current flashcard

    // Update the UI with the new flashcard content
    document.getElementById('flashcard-front').textContent = currentFlashcard.front;
    document.getElementById('flashcard-back').textContent = currentFlashcard.back;
}

function dropFlashcard(flashcard) {
    const index = flashcardsArray.findIndex(card => card.front === flashcard.front && card.back === flashcard.back);
    if (index !== -1) {
        flashcardsArray.splice(index, 1); // Remove the flashcard from the array
        console.log('Flashcard removed from array', flashcard);
        console.log('Flashcards array:', flashcardsArray);
    } else {
        console.log('Flashcard not found in array');
    }
}


function checkAnswer() {
    const answer = document.getElementById('answer').value;
    const answerInput = document.getElementById('answer');
    const capitalizedAnswer = answer.charAt(0).toUpperCase() + answer.slice(1).toLowerCase();
    const flashcardBack = document.getElementById('flashcard-back').textContent;

    if (capitalizedAnswer === flashcardBack) {
        console.log('Correct!');
        answerInput.style.transition = 'background-color 0.5s ease';
        answerInput.style.backgroundColor = 'lightgreen';
        setTimeout(() => {
            answerInput.style.backgroundColor = '';
        }, 1000); // Fade out after 1 second
        setTimeout(() => {
            answerInput.value = ''; // Clear the answer input after fade out
        }, 1000); // Clear after fade out completes
        
        // Remove the current flashcard and show a new one
        if (currentFlashcard) {
            dropFlashcard(currentFlashcard); // Remove the correct card from the array
        }
        if (document.getElementById('flashcard').classList.contains('flipped')) {
            document.getElementById('flashcard').classList.remove('flipped');
        }
        setTimeout(() => {
            showNextCard(); // Show a new flashcard after a short delay
        }, 500);

        // Update score
        const currentScoreElement = document.getElementById('current-score');
        currentScoreElement.textContent = parseInt(currentScoreElement.textContent) + 1;
    } else {
        console.log('Incorrect!');
    }
}