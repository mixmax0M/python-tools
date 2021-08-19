from time import sleep
from datetime import datetime
import requests, random, json, string
import concurrent.futures

def GetGame(id):
    r = requests.get(f"https://kahoot.it/reserve/session/{id}")
    return r

def GetCode(rangue):
    num = ""
    for i in range(rangue):
        num = num + random.choice(string.digits)
        i =+ 1
    return num

def Finder():
    sleep(0.04)
    code = GetCode(7)
    reasons = GetGame(code).reason
    stcode = GetGame(code).status_code

    if reasons == "OK":
        print("Working code found! -> " + code + f" Reason -> {reasons}")
        time = datetime.now().strftime("%H:%M:%S")
        f = open("kcodes.txt", "a")
        f.write(f"{code} Time -> {time}\n")
    elif stcode == 503:
        sleep(0.5)
    else:
        pass

def Minder():
    code = GetCode(6)
    reasons = GetGame(code).reason
    stcode = GetGame(code).status_code

    if reasons == "OK":
        print("Working code found! -> " + code + f" Reason -> {reasons}")
        time = datetime.now().strftime("%H:%M:%S")
        f = open("kcodes.txt", "a")
        f.write(f"{code} Time -> {time}\n")
    elif stcode == 503:
        sleep(0.5)
    else:
        pass

threads = int(input("Input the amount of threads: "))

while True:
    with concurrent.futures.ThreadPoolExecutor() as executer:
        results = [executer.submit(Finder) for _ in range(threads)]
        mesults = [executer.submit(Minder) for _ in range(threads)]
