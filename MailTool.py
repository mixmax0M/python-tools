import requests, random, json, string

API = "https://www.1secmail.com/api/v1/"

# Gets all active domains from the API
def GetDomainList():
    r = requests.get(API + "?action=getDomainList")
    formatted = r.text.replace("[", "").replace('"', "").replace("]", "").split(",")
    return formatted

#Creates random email
def CreateRandomEmail(count):
    r = requests.get(API + f"?action=genRandomMailbox&count={count}")
    formatted = r.text.replace("[", "").replace('"', "").replace("]", "")
    return formatted

#Checks Mailbox of selected email
def CheckMailbox(login, domain):
    r = requests.get(API + f"?action=getMessages&login={login}&domain={domain}")
    return r.text

# Checks single message
def CheckMessage(login, domain, id):
    r = requests.get(API + f"?action=readMessage&login={login}&domain={domain}&id={id}")
    return r.text

# Downloads a attachment from selected msg
def DownloadAttchment(login, domain, id, attch):
    r = requests.get(API + f"?action=download&{login}=demo&domain={domain}&id={id}&file={attch}")
    print("Download Complete!")
    return r
