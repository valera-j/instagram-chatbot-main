import os
from instagrapi import Client
from apscheduler.schedulers.background import BackgroundScheduler

# Retrieve username and password from environment variables
username = os.environ['INSTAGRAM_USERNAME']
password = os.environ['INSTAGRAM_PASSWORD']

api = Client()
api.login(username, password)

def generate_response(message_text):
    message_text = message_text.lower()

    if "playlist" in message_text:
        return "Here is the playlist link: [your_playlist_link] 🎧🎵"
    elif "hello" in message_text:
        return "Hi there! How can I help you today? 🥰"
    elif "contact" in message_text:
        return "You can contact us at [your_contact_email] or [your_phone_number]."
    # Add more conditions here
    else:
        return None

def process_messages():
    print("Checking for new messages...")
    all_conversations = api.direct_threads(selected_filter="unread")

    if not all_conversations:
        print("No new messages found.")

    for conversation in all_conversations:
        thread_id = conversation.id
        last_message = conversation.messages[0]

        if last_message.user_id != api.user_id and last_message.text is not None:
            response = generate_response(last_message.text)
            if response:
                api.direct_answer(thread_id, response)

                # Print message status
                print(f"Responded to message: {last_message.text}")


def schedule_process_messages():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_messages, 'interval', seconds=30)
    scheduler.start()

if __name__ == "__main__":
    print("Starting chatbot...")
    schedule_process_messages()

    # Keep the script running
    while True:
        pass
