import requests
import configparser

def get_ai_response(text):
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    api_key = config['openai']['api_key']

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': text}]
    }
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error during OpenAI API request: {e}")
        return "I'm sorry, I encountered an error."

if __name__ == '__main__':
    # Example usage (replace with your actual API key in config.ini)
    response = get_ai_response("What is the capital of France?")
    print(response)
