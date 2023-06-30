from flask import Flask, Response
import telebot
import random
import requests

# Create a new instance of the bot
# bot = telebot.TeleBot('6136687473:AAFCjhjpwcfRce8RTG0TK_JiLzA8kolwVvM')

# Create a Flask web application
app = Flask(__name__)


# # Handle the /start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Welcome to personify, your unbiased companion!🤖\n\npersonify is here to help you uncover and challenge unconscious bias in your everday interactions.\n\n🔹To get started, simply type /join and let the exploration begin!\n🔹 For a list of available commands, type /help.\n🔹 To learn more about the purpose and functionality of personify, type /info.\n\nHappy exploring with personify!✨")
    
# # Handle the /info command
# @bot.message_handler(commands=['join'])
# def join(message):
#     bot.send_message(message.chat.id, "We're excited to have you onboard!🤝 \n This is how personify works:\n\n1️⃣ You will receive a short prompt describing someone. \n2️⃣ You'll need to respond with your impression of the person in a single message. Impressions can include, but are not exclusive to the gender, race, physical appearance, character traits, educational background, social class and sexual orientation of the person. You do not have to touch on every category if your impression is neutral in those aspects.\n3️⃣ We will evaluate your response and provide feedback on how unconscious bias was present in your impression.\n\nOnce you are ready, type /prompt to begin!")

# # Define the list of predefined messages
# prompts = [
#     "Social Worker",
#     "Famous Social Media Influencer",
#     "President of a country",
#     "Convicted criminal",
#     "CEO of a tech company",
#     "Investment Banker", 
#     "Software Engineer",
#     "Marketing Director",
#     "Dictator", 
#     "Breadwinner of a household",
#     "Valedictorian"
# ]
# # Empty variable to enable prompts not duplicated
# sent_prompts = []
    
# response_sent = False  # Flag to track if a response has been sent for the current prompt

# # Handle the "/prompt" command
# @bot.message_handler(commands=['prompt'])
# def prompt(message):
#     global response_sent

#     # Check if all prompts have been used
#     if len(sent_prompts) == len(prompts):
#         bot.send_message(message.chat.id, "All prompts have been used. Type /reset to start again.")
#         return

#     # Randomly select a message from the list
#     selected_prompt = random.choice(prompts)
#     # Check if the selected message has been sent before
#     while selected_prompt in sent_prompts:
#         selected_prompt = random.choice(prompts)

#     # Send the selected message as a reply
#     response = "Describe your impression of this person: \n\n" + selected_prompt
#     bot.send_message(message.chat.id, response)

#     # Add the selected message to the sent prompts list
#     sent_prompts.append(selected_prompt)

#     response_sent = False  # Reset the flag for a new prompt
    
    
# # Handle the /help command
# @bot.message_handler(commands=['help'])
# def help_command(message):
#     commands = [
#         '/start - Start the bot',
#         '/join - Receive instructions',
#         '/help - Show available commands',
#         '/prompt - Receive your prompt',
#         '/reset - Reset bot'
#     ]
#     help_text = "Available commands:\n\n" + "\n".join(commands)
#     bot.send_message(message.chat.id, help_text)


# # Handle the "/reset" command
# @bot.message_handler(commands=['reset'])
# def reset(message):
#     # Clear the list of sent messages
#     sent_prompts.clear()
#     bot.reply_to(message, "Bot has been reset.")
    

# # Replace "YOUR_API_ENDPOINT" with the actual ChatGPT API endpoint
# api_endpoint = "https://api.pawan.krd/v1/chat/completions"

# # Function to send user input to the ChatGPT API
# def send_to_chatgpt(user_input):
#     # Set up the API request payload
#     payload = {
#         "messages": [
#             {"role": "system", "content": "prompt"},
#             {"role": "user", "content": user_input}
#         ],
#         "temperature": 0.5,  # Adjust temperature value as needed
#         "max_tokens": 1500  # Adjust max tokens value as needed
#     }
#     headers = {'content-type': 'application/json', "Authorization": "Bearer pk-xpCZtZfUyiOBDdEVcTUEriUXaySHMJnpGwdWVQULZdyoRWDO"}

#     try:
#         # Send the request to the API endpoint
#         response = requests.post(api_endpoint, json=payload, headers = headers)

#         # Parse and return the generated response from the API
#         api_response = response.json()
#         generated_response = api_response#["choices"][0]["message"]["content"]
#         print(generated_response)
#         return generated_response
#     except requests.exceptions.RequestException as e:
#         print("Error occurred:", e)
#         return None


# # Handle incoming messages
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     global response_sent

#     # Check if the message is a text message
#     if message.content_type == "text":
#         # Get the user's input from the message
#         user_input = message.text

#         # Check if a response has already been sent for the current prompt
#         if not response_sent:
#             # Send user input to the ChatGPT API
#             generated_response = send_to_chatgpt('How is this description of ' + sent_prompts[-1] + ' inherently biased: ' + user_input + ' and what would be a more accurate depiction of ' + sent_prompts[-1] + ' and real-life examples of these individuals who differ from my description?' +' . Additionally, what are some steps I can take to reduce my unconscious bias?')

#             if generated_response:
#                 # Send the generated response back to the user
#                 bot.send_message(message.chat.id,generated_response)

#             response_sent = True  # Update the flag after sending the response

# # 

@app.get("/")    
def home():
    return "Hello world!"

if __name__ == "__main__":
   app.run(debug=True, port = 5001)