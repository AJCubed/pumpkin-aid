# Flask-OpenAI-Chatbot
A Flask chatbot application that can schedule hospital appointments.

## Features
- Utilize OpenAI's GPT-3.5 Turbo for intelligent responses.
- User-friendly chatbot interface built with HTML and Flask.
- Store chat history for each conversation in text files.

## Getting Started

### Prerequisites

- Python 3.7+ installed on your system.
- Flask 2.0.1 and OpenAI Python SDK installed.
- Set up your OpenAI API key.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AJCubed/vandyhacks
    ```

2. 2. Navigate to the project directory:https://github.com/AJCubed/vandyhacks
```bash
cd vandyhacks
```
3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
This command will install all the necessary Python packages and dependencies required for your chatbot application.

4. Configure your OpenAI API key:
In order to use OpenAI's GPT-3.5 Turbo for intelligent responses in your chatbot, you'll need to configure your OpenAI API key in the app.py file. Follow these steps:
Create a .env file outside the app folder
Paste in your API key; it should look like this:
```python
OPENAI_API_KEY = "sk-zqn9OVmS71IvKsg10nFiTsgRykFJxlMij3WPbmeegvhzPB2p"
```

5. Usage
Now that you've completed the setup, you can use your Chatbot App:
a. Start the Flask app:
```bash
flask run
```
b. Open your web browser and go to http://localhost:5000 to interact with the chatbot.
Tell it about your symptoms and when you'd like to schedule an appointment, and watch as the database updates with your new info.