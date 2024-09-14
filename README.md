# Language Flashcards

Language Flashcards is a web application designed to help users learn and practice vocabulary in different languages using digital flashcards.

## Distinctiveness and Complexity

This project satisfies the distinctiveness and complexity requirements for the following reasons:

1. **Unique Purpose**: Unlike typical social media or e-commerce platforms, this application focuses on language learning, offering a specialized tool for vocabulary acquisition.

2. **Interactive Learning**: The app provides an interactive study session feature, allowing users to flip cards, input answers, and receive immediate feedback.

3. **User-Specific Content**: Users can create, edit, and manage their own decks and flashcards, tailoring the learning experience to their needs.

4. **Progress Tracking**: The application includes a scoring system and tracks user progress across study sessions.

5. **Responsive Design**: The user interface is designed to be responsive, ensuring a seamless experience across various devices.

6. **Complex Data Management**: The backend handles complex relationships between users, decks, and flashcards, including creation, updating, and deletion operations.

7. **AJAX Integration**: The study session feature uses AJAX to dynamically load new flashcards without page reloads, enhancing the user experience.

## File Contents

- `models.py`: Contains the database models for User, Deck, Flashcard, and StudySession.
- `views.py`: Includes all the view functions for rendering pages and handling form submissions.
- `urls.py`: Defines the URL patterns for the application.
- `forms.py`: Contains form classes for user input validation.
- `admin.py`: Configures the admin interface for managing application data.
- `static/flashcards/`:
  - `styles.scss`: Contains all the SCSS styles for the application.
  - `script.js`: Includes JavaScript for interactive features like flipping cards and AJAX requests.
- `templates/flashcards/`: Contains all HTML templates for rendering pages.

## How to Run the Application

1. Ensure you have Python and Django installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in the terminal.
4. Run `python manage.py migrate` to set up the database.
5. Run `python manage.py runserver` to start the development server.
6. Open a web browser and go to `http://localhost:8000` to access the application.

## Additional Information

- The application uses SCSS for styling. Make sure to compile the SCSS files to CSS before running the application in a production environment.
- The project includes custom user authentication and registration system.

## App Features

1. **User Authentication**: Register, login, and logout functionality.
2. **Deck Management**: Create, edit, and delete decks of flashcards.
3. **Flashcard Creation**: Add, edit, and delete flashcards within decks.
4. **Study Session**: Interactive study mode with card flipping and answer input with the case support.
5. **Progress Tracking**: Score display and session history.
6. **User Profile**: View and manage personal decks and study statistics.
7. **Responsive Design**: Optimized for both desktop and mobile devices.
9. **Language Selection**: Create decks for different languages.
