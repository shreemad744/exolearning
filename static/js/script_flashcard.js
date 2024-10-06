// Filter functionality
const searchInput = document.getElementById('searchInput');
const flashcards = document.querySelectorAll('.flashcard');

searchInput.addEventListener('input', function() {
    const filter = searchInput.value.toLowerCase();
    flashcards.forEach(flashcard => {
        const question = flashcard.querySelector('.front h3').textContent.toLowerCase();
        const topic = flashcard.getAttribute('data-topic').toLowerCase();
        if (question.includes(filter) || topic.includes(filter)) {
            flashcard.style.display = 'flex';
        } else {
            flashcard.style.display = 'none';
        }
    });
});
