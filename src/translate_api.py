import requests
import json

failed_retries = 0

def translate(text: str = 'Hello, world!',
              source_language: str = 'en',
              destination_language: str = 'es',
              ip: str = '192.168.52.98') -> object:
    """Translate text from source_language to destination_language. Language codes are ISO 639-1 codes."""
    print(text, ":", source_language, " ------> ", destination_language)

    global failed_retries
    url = f'http://{ip}:5000/translate'
    text = requests.utils.quote(bytes(text, 'utf8'))
    params = {'text': text, 'src': source_language, 'dst': destination_language}
    if failed_retries < 3:
        try:
            response = requests.get(url, params=params)
            response_text = requests.utils.unquote(response.text)
        # print(response_text)
        # print(type(response_text))
            failed_retries = 0
            print(response_text)
            return response_text
        except requests.exceptions.ConnectionError as e:
            print(e)
            failed_retries += 1
            return 'Nie ma połączenia'
    else:
        return 'Nie ma połączenia'

