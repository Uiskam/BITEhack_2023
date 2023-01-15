import requests
import json


def translate(text: str = 'Hello, world!',
              source_language: str = 'en',
              destination_language: str = 'es',
              ip: str = '192.168.52.98') -> object:
    """Translate text from source_language to destination_language. Language codes are ISO 639-1 codes."""

    url = f'http://{ip}:5000/translate'
    text = requests.utils.quote(text)
    params = {'text': text, 'src': source_language, 'dst': destination_language}
    response = requests.get(url, params=params)
    return json.loads(response.text)
