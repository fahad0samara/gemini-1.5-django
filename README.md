
## Chat AI Application

This project is a simple Chat AI application built using Django and JavaScript. It utilizes the Gemini API for text generation and features a responsive interface for interacting with the AI.

### Key Features

- **Responsive Interface**: The application features a clean, responsive interface built with HTML, CSS, and JavaScript. The layout is designed to work well across various screen sizes.

- **Conversation History**: The sidebar on the left side of the interface displays the history of all conversations. Each conversation is labeled with the first three words of the prompt, making it easy to navigate through past interactions.

- **New Chat and Delete History**: You can start a new conversation at any time by clicking the "New Chat" button. Additionally, there is a "Delete All History" button that allows you to clear the entire conversation history. This button is only visible if there is existing history.

- **Local Storage**: Conversations are saved in the browser's local storage, allowing you to refresh the page without losing past conversations.

- **Markdown Support**: The application supports Markdown formatting for both prompts and AI responses, providing a richer text display.

### How to Use

1. **Start a Conversation**: Type your message in the input field at the bottom and click "Send". The AI's response will appear in the chat window above.
   
2. **View Conversation History**: Click on any conversation in the history list to view it in the chat window. The list shows the first three words of the prompt for easy identification.

3. **Clear History**: If you want to delete all conversation history, click the "Delete All History" button. This action will remove all stored conversations from local storage.

### Technologies Used

- **Django**: Backend framework to manage API requests and responses.
- **JavaScript**: Handles the frontend logic, including updating the chat window and managing local storage.
- **Gemini API**: Powers the text generation feature, providing responses to user prompts.
- **HTML/CSS**: Defines the structure and style of the application, ensuring a user-friendly experience.

### Setup Instructions

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/fahad0samara/gemini-1.5-django.git
   ```
2. Navigate to the project directory:
   ```bash
   cd gemini-1.5-django
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and navigate to `http://localhost:8000` to start interacting with the Chat AI application.





