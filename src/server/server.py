#!/usr/bin/env python3

from flask import Flask, request
from translate_proxy import translate_text
import json
import requests

app = Flask(__name__)


@app.route('/')
def greet():
    return 'enter http://IP:5000/translate?text=TEXT to translate from english to spanish'


@app.route('/translate', methods=['GET'])
def translate():
    try:
        text = request.args.get('text')
        source_language=request.args.get('src')
        destination_language=request.args.get('dst')
    except KeyError as e:
        return 'Incorrect parameters. Please enter http://IP:5000/translate?text=TEXT&src=en&dst=es to translate from english to spanish'

    print(f'text1: {text}')
    text = requests.utils.unquote(text)
    print(f'text2: {text}')

    results = translate_text(text, source_language, destination_language)

    return json.dumps(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')