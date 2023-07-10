import openai
import logging

ENGINE = "gpt-4-0613"
MAX_TOKENS = 4000
TEMPERATURE = 0.0

def get_response(api_key, messages, engine=ENGINE, max_tokens=MAX_TOKENS, temperature=TEMPERATURE):
    try:
        openai.api_key = api_key
        chat_completion = openai.ChatCompletion.create(
                          model=engine,
                          messages=messages, 
                          max_tokens=max_tokens, 
                          temperature=temperature)
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Failed to get response from API. Error: {e}")
        return None