Instagram Chatbot README
This Instagram chatbot is designed to automatically respond to incoming direct messages based on the message content. The chatbot can handle various types of messages, such as requests for a playlist link, contact information, and more.

Getting Started
Prerequisites
Python 3.6 or later
An Instagram account with username and password
Installing Dependencies
This project requires the following Python libraries:

instagrapi
apscheduler
To install these libraries, you can use the provided requirements.txt file. Run the following command in your terminal:
```
bash
Copy code
pip install -r requirements.txt
```
Configuration
To set up the Instagram chatbot, you need to provide your Instagram account credentials in the config.txt file. The file should look like this:
```
username=your_username
password=your_password
```
Replace your_username and your_password with your actual Instagram username and password.

Running the Chatbot
To start the chatbot, run the following command in your terminal:

```
bash
python app.py
```
The chatbot will now periodically check for new unread messages in your Instagram direct messages and respond accordingly.

Customizing Responses
To add more responses or modify the existing ones, update the generate_response() function in the app.py file. For example:
```
python
def generate_response(message_text):
    message_text = message_text.lower()

    if "keyword1" in message_text:
        return "Your response for keyword1"
    elif "keyword2" in message_text:
        return "Your response for keyword2"
    # Add more conditions here writing another elif
    else:
        return None
        
```
Replace keyword1, keyword2, and their corresponding responses with the desired keywords and responses.


As a reminder, for this program to work, need to be running in your computer