# Import necessary libraries
from flask import Flask, render_template, request, redirect
import openai
import os
import time
from dotenv import load_dotenv
load_dotenv()

# Set the OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define the name of the bot
name = 'BOT'

# Define the role of the bot
role = 'Hospital Front Desk'

# Define the impersonated role with instructions
impersonated_role = f"""
    You are a hospital front desk AI agent. Patients are coming to you for help scheduling appointments for various illnesses.
    You must establish all of these details during the conversation. However, please speak at a natural pace, but professionally without reciting these questions word-for-word.
        1. "May I have your name and birthday to access your record?"
        2. What symptoms have they been having? Are there any others? Ask until they have no more issues to report.
        3. How long have symptoms been going on?  How severe are they (mild, moderate, severe)? 
        3. Suggest a hospital department suitable for treating them (cardiology for breathing issues, etc), and ask if they would like to schedule an appointment.
        4. If they would like an appointment, ask for a preferred date and tell the user their appointment will be scheduled shortly. If not, cordially end the conversation.
"""

output_format = f"""
    Extract these details into a JSON file with this exact format:
        {{
            "name": string
            "birthday": date
            "symptoms" : [string, string]
            "summary": string
            "apptDate": date
        }}
    Birthday and apptDate should be of mm-dd-yy types (if it's entered as a word, convert it), 
    Symptoms should be only keywords, and summary should be a short paragraph of the symptoms, severity, and duration for doctor reference.
"""

# Initialize variables for chat history
explicit_input = ""
chatgpt_output = 'Chat log: /n'
cwd = os.getcwd()
i = 1

# Find an available chat history file
while os.path.exists(os.path.join(cwd, f'chat_history{i}.txt')):
    i += 1

history_file = os.path.join(cwd, f'chat_history{i}.txt')

# Create a new chat history file
with open(history_file, 'w') as f:
    f.write('\n')

# Initialize chat history
chat_history = ''

# Create a Flask web application
app = Flask(__name__)

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, impersonated_role, explicit_input, chat_history):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Conversation history: {chat_history}"},
            {"role": "user", "content": f"{user_input}. {explicit_input}"},
        ]
    )

    for item in output['choices']:
        chatgpt_output = item['message']['content']

    return chatgpt_output

# Function to handle user chat input
def chat(user_input):
    global chat_history, name, chatgpt_output
    current_day = time.strftime("%d/%m", time.localtime())
    current_time = time.strftime("%H:%M:%S", time.localtime())
    chat_history += f'\nUser: {user_input}\n'
    chatgpt_raw_output = chatcompletion(user_input, impersonated_role, explicit_input, chat_history).replace(f'{name}:', '')
    chatgpt_output = f'{chatgpt_raw_output}'
    chat_history += chatgpt_output + '\n'
    with open(history_file, 'a') as f:
        f.write('\n'+ current_day+ ' '+ current_time+ ' User: ' +user_input +' \n' + current_day+ ' ' + current_time+  ' ' +  chatgpt_output + '\n')
        f.close()
    return chatgpt_raw_output

# Function to get a response from the chatbot
def get_response(userText):
    if "thank you" in userText.lower():
        generate_json_summary(history_file)
        return "No problem!"
    return chat(userText)

def generate_json_summary(filename):
    with open(filename, 'r') as f:
        content = f.read()

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Read this following conversation transcript\n\n{content}\n\nOutput format: {output_format}"}
    ]

    output = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=2000,
        messages=messages
    )
    print(output.choices[0].message["content"])


# Define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))

@app.route('/refresh')
def refresh():
    time.sleep(600) # Wait for 10 minutes
    return redirect('/refresh')

# Run the Flask app
if __name__ == "__main__":
    generate_json_summary("chat_history.txt")
    # app.run()
