from google.cloud import translate
from iso639 import languages
import random
import requests

def translate_text(text: str ="Hello, world!", source_language: str ='en-US', destination_language: str ='es'):

    if languages.get(alpha2=source_language) and languages.get(alpha2=destination_language):
        pass
    else:
        return "Invalid language code"


    client = translate.TranslationServiceClient()
    project_id="bitehack2023"
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": source_language,
            "target_language_code": destination_language,
        }
    )

    print(f'text: {text}')
    print(source_language)
    print(destination_language)
    print(response.translations[0])

    translations=[]
    for translation in response.translations:
        translations.append(translation.translated_text)
    return requests.utils.quote(translations[0])
    # return translations[0]

    # random_return = random.choice(['Nie tym razem', 'Chciałbyś...', 'Otóż nie'])

    # return requests.utils.quote(random_return)


if __name__ == '__main__':
    result = translate_text(text="Hello, world!", source_language='en', destination_language='es')
    print(result)
