import openai
import logging

class OpenAI_API:
    def __init__(self, api_key, engine="gpt-4-0613", max_tokens=4000, temperature=0.0):
        self.api_key = api_key
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        openai.api_key = self.api_key

    def get_response(self, messages):
        try:
            chat_completion = openai.ChatCompletion.create(
                              model=self.engine,
                              messages=messages, 
                              max_tokens=self.max_tokens, 
                              temperature=self.temperature)
            return chat_completion.choices[0].message.content
        except Exception as e:
            logging.error(f"Failed to get response from API. Error: {e}")
            return None