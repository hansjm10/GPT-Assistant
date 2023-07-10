import os
from file import read_file, write_to_file

CONVERSATION_FOLDER = 'conversations'

def get_messages(conversation_id):
    conversation_folder = os.path.join(CONVERSATION_FOLDER, conversation_id)
    if not os.path.exists(conversation_folder):
        os.makedirs(conversation_folder)
        return []
    message_files = os.listdir(conversation_folder)
    messages = []
    for message_file in message_files:
        message = read_file(os.path.join(conversation_folder, message_file))
        if message is not None:
            role, content = message.split('\n', 1)
            messages.append({"role": role, "content": content})
    return messages

def add_message(conversation_id, role, content):
    conversation_folder = os.path.join(CONVERSATION_FOLDER, conversation_id)
    message_file = os.path.join(conversation_folder, f"{len(os.listdir(conversation_folder)) + 1}.txt")
    write_to_file(f"{role}\n{content}", message_file)