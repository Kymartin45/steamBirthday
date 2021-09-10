import requests
from requests import api
import json 
import time
import argparse

key = 'STEAM API KEY'

print('Steam Birthday 🎂 \n-----------------')
print("Note: Must enter your SteamID (Custom URL name)\nDon't know your Steam ID? Check out the link below!\n")
print('https://www.maketecheasier.com/find-steam-id/\n')

parser = argparse.ArgumentParser()
parser.add_argument('--steamid', type=str, required=True)
args = parser.parse_args()

def getId():
    req_url = f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={key}&vanityurl={args.steamid}'
    api_res = requests.get(req_url)
    res = api_res.json()
    steamId = res['response']['steamid']
    return steamId

getIdFunc = getId()

def getPlayerSummary():
    req_url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={getIdFunc}'
    api_res = requests.get(req_url)
    res = api_res.json()
    steamSummary = res['response']['players'][0]['timecreated']
    return steamSummary

getSummary = getPlayerSummary()
dateFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(getSummary))
print('Account created:', dateFormat)

