import requests

def Agents():
    r = requests.get("https://valorant-api.com/v1/agents")
    if r.status_code == 200:   
        json_data = r.json()
        return json_data
    else:
        return "Something went wrong"
    
def Maps():
    r = requests.get("https://valorant-api.com/v1/maps")
    if r.status_code == 200:   
        json_data = r.json()
        return json_data
    else:
        return "Something went wrong"
    
def Weapon():
    r = requests.get("https://valorant-api.com/v1/weapons")
    if r.status_code == 200:   
        json_data = r.json()
        return json_data
    else:
        return "Something went wrong"
    
def Card():
    r = requests.get("https://valorant-api.com/v1/playercards")
    if r.status_code == 200:
        json_data = r.json()
        return json_data
    else:
        return "something went wrong"