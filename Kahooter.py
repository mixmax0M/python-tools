from time import sleep
import requests, random, json, string
import concurrent.futures

def GetGame(id):
    r = requests.get(f"https://kahoot.it/reserve/session/{id}")
    return r

def GetCode():
    num = ""
    for i in range(6):
        num = num + random.choice(string.digits)
        i =+ 1
    return num

def Finder():
    sleep(0.4)

    code = GetCode()
    reasons = GetGame(code).reason
    stcode = GetGame(code).status_code

    if reasons == "OK":
        print("Working code found! -> " + code + f" Reason -> {reasons}")
    else:
        print("Code: " + code + " failed. Status code -> " + str(stcode) + " Reason -> " + reasons)

threads = input("Input the amount of threads: ")

while True:
    with concurrent.futures.ThreadPoolExecutor() as executer:
        results = [executer.submit(Finder) for _ in range(threads)]
#        for f in concurrent.futures.as_completed(results):
#           print("")