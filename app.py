import os
from re import X
import openai
import requests
from decouple import config 
import random
import re


# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
# make .env file without name then write inside .env: API_KEY=sk..
# and call with config

openai.api_key= config('API_KEY_MIRO')
board_id = "uXjVO6mflkg="
url = f'https://api.miro.com/v1/boards/{board_id}/widgets/'

headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": f'Bearer {openai.api_key}'}

def make_card(text:str):
    payload = {
        "type": "sticker",
        "text": f'<p>{text}</p>',
        "x": random.randint(0,180), 
        "y": random.randint(0,180) # x and y are axis
        }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

#make_card("Team Spacy")

def get_card() -> list:
    response = requests.request("GET", url, headers=headers)
    list_of_text = []
    flat_list = []
    for sentence in response.json()["data"]:
        regex = '^text'
        text = [v for k, v in sentence.items() if re.match(regex, k)]
        new_text = [x.replace("<p>", "").replace("</p>", "") for x in text]
        list_of_text.append(text)
        for sublist in list_of_text:
            for item in sublist:
                flat_list.append(item)              
    return flat_list
        
get_card = get_card()
print(get_card)

