import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures
import string

def getProxies(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='HTTP' or 'HTTPS':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies

proxyyy = ["https://www.netzwelt.de/proxy/index.html/", "https://free-proxy-list.net/"] 
for prrrs in proxyyy:
    proxylist = getProxies(prrrs)
    for element in proxylist:
            print(element)
