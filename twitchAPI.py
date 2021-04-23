import requests, json, sys

BASE_URL = 'https://api.twitch.tv/helix/'
file = open("accessTokens.gitignore", 'r')
file = json.load(file)
CLIENT_ID = file["ClientID"]
ACCESS_TOKEN = file["AccessToken"]
SECRET = file["Secret"]
HEADERS = {'client-id' : CLIENT_ID, 
    "Authorization" : "Bearer " + ACCESS_TOKEN}
INDENT = 2


def get_user_id(user):
    url = BASE_URL + 'search/channels?query=' + user
    response = requests.get(url, headers=HEADERS)
    response = response.json()
    print(response)

def get_stream(user):
    url = BASE_URL + 'streams?user_login=' + user
    r = requests.get(url,headers = HEADERS)
    r = parseResponse(r)
    return r

def parseResponse(response):
    response = response.json()
    return response

def get_channel(user):
    url = BASE_URL + user
    response = requests.get(url, headers=HEADERS)
    print(response)

def getAccessToken(secret):
    url = 'https://id.twitch.tv/oauth2/token?client_id=' + CLIENT_ID + '&client_secret=' + secret + '&grant_type=client_credentials'
    response = requests.get(url)
    print(response)
