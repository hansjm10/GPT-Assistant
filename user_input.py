import os
import logging

DEFAULT_SYSTEM_FILE = 'system.txt'
CODE_REVIEW_FILE = 'code_review_system.txt'
TEST_WRITER_FILE = 'test_writer_system.txt'

SYSTEM_FILES = {
    1: DEFAULT_SYSTEM_FILE,
    2: CODE_REVIEW_FILE,
    3: TEST_WRITER_FILE,
}

def get_user_choice():
    while True:
        for choice, system_file in SYSTEM_FILES.items():
            print(f"{choice}. {system_file}")
        choice = input("Enter your choice: ")
        if choice.isdigit() and int(choice) in SYSTEM_FILES:
            return int(choice)
        print(f"Invalid choice. Please enter a number between 1 and {len(SYSTEM_FILES)}.")


def get_conversation_id():
    conversation_id = input("Enter the conversation ID (or 'new' to start a new conversation): ")
    if conversation_id == 'new':
        conversation_id = input("Enter a name for the new conversation: ")
    return conversation_id