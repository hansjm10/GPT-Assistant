import unittest
from unittest.mock import patch, MagicMock
import os
import api
import conversation
import file
import main
import user_input

API_KEY = os.getenv('OPENAI_API_KEY')

class TestAPI(unittest.TestCase):
    @patch('openai.ChatCompletion.create')
    def test_get_response(self, mock_create):
        mock_create.return_value.choices[0].message.content = 'Test response'
        response = api.get_response(API_KEY, [])
        self.assertEqual(response, 'Test response')

class TestConversation(unittest.TestCase):
    @patch('os.makedirs')
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('file.read_file')
    def test_get_messages(self, mock_read_file, mock_listdir, mock_exists, mock_makedirs):
        mock_exists.return_value = False
        messages = conversation.get_messages('fake_conversation_id')
        self.assertEqual(messages, [])
        mock_makedirs.assert_called()

    @patch('os.makedirs')
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('file.write_to_file')
    def test_add_message(self, mock_write_to_file, mock_listdir, mock_exists, mock_makedirs):
        mock_exists.return_value = True
        mock_listdir.return_value = ['1.txt']
        conversation.add_message('fake_conversation_id', 'user', 'Test message')
        mock_write_to_file.assert_called()

class TestFile(unittest.TestCase):
    @patch('builtins.open')
    def test_read_file(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = 'Test content'
        content = file.read_file('fake_file.txt')
        self.assertEqual(content, 'Test content')

    @patch('builtins.open')
    def test_write_to_file(self, mock_open):
        file.write_to_file('Test response', 'fake_file.txt')
        mock_open.assert_called_with('fake_file.txt', 'a')

class TestMain(unittest.TestCase):
    @patch('os.getenv')
    @patch('logging.error')
    def test_main_no_api_key(self, mock_error, mock_getenv):
        mock_getenv.return_value = None
        main.main()
        mock_error.assert_called_with("Error: The OPENAI_API_KEY environment variable is not set.")

class TestUserInput(unittest.TestCase):
    def test_get_user_choice(self):
        with patch('builtins.input', return_value='1'):
            choice = user_input.get_user_choice()
            self.assertEqual(choice, 1)

    def test_get_conversation_id(self):
        with patch('builtins.input', return_value='new'):
            conversation_id = user_input.get_conversation_id()
            self.assertEqual(conversation_id, 'new')

if __name__ == '__main__':
    unittest.main()