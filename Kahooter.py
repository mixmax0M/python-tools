from time import sleep
import requests, random, json, string

def GetGame(id):
    r = requests.get(f"https://kahoot.it/reserve/session/{id}")
    return r

def GetCode():
    num = ""
    for i in range(6):
        num = num + random.choice(string.digits)
        i =+ 1
    return num

sleep(5)
while True:
    sleep(0.4)

    code = GetCode()
    reasons = GetGame(code).reason
    stcode = GetGame(code).status_code

    if reasons == "OK":
        print("Working code found! ->" + code)
    else:
        print("Code: " + code + " failed. Status code -> " + str(stcode) + " Reason -> " + reasons)
