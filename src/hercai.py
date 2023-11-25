import requests
import json

def qeaHercai(text):
    response = requests.get(f'http://localhost:3000/hercai/?q={text}')
    return response.json()

def translateHercai(text, from_lang, to_lang):
    response = requests.get(f'http://localhost:3000/hercai/translate?q={text}&from={from_lang}&to={to_lang}')
    return response.json()

def summarizeHercai(text):
    response = requests.get(f'http://localhost:3000/hercai/sumup?q={text}')
    return response.json()

def get_keywordsHercai(text, keyNum):
    response = requests.get(f'http://localhost:3000/hercai/keys?q={text}&key={keyNum}')
    return response.json()
