import logging
import os
from api import get_response
from file import read_file, write_to_file
from user_input import get_user_choice, get_conversation_id, SYSTEM_FILES
from conversation import get_messages, add_message
from api import OpenAI_API

API_KEY = os.getenv('TEST_OPENAI_SECRET_KEY')
PROMPT_FILE = 'prompt.txt'
CODE_FILES = ['api.py', 'conversation.py', 'file.py', 'main.py', 'user_input.py']

def main():
    if API_KEY is None:
        logging.error("Error: The TEST_OPENAI_SECRET_KEY environment variable is not set.")
        return

    openai_api = OpenAI_API(API_KEY)

    choice = get_user_choice()
    system_file = SYSTEM_FILES[choice]

    system = read_file(system_file)
    prompt = read_file(PROMPT_FILE)
    code = ""
    for code_file in CODE_FILES:
        code += '``` ' + code_file + '\n' + read_file(code_file) + '\n```'
        

    if system is None or prompt is None or code is None:
        return
    write_to_file(code, 'code.txt')
    conversation_id = get_conversation_id()
    messages = get_messages(conversation_id)
    messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt + '\n' + code})

    response = openai_api.get_response(messages)
    add_message(conversation_id, "assistant", response)

if __name__ == "__main__":
    main()
