import requests
import json

def Sender(datas):

    data = {
        "key1": "val1",
        "key2": "val2"
    }
    url = "URL HERE"

    response = requests.post(url, data)
    print(response)

# Txt file example
with open('example.txt','r') as file:
    for line in file:
        for word in line.split():
            Sender(word)
