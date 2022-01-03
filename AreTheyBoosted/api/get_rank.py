import api_request as api
import requests

def get_rank(name, region):
    response = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    print(response.json())


get_rank("Reese", "OC1")

