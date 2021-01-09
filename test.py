import discord
import requests
import requests

r = requests.get("https://valorant-api.com/v1/weapons")
json_data = r.json()
print(json_data['data'][13]['weaponStats']['adsStats']['zoomMultiplier'])