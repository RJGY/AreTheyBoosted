import regions
import requests
import api_request as api

def get_uuid(name, region):    
    region = regions.region_converter_fullname(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    return summoner.json().get("id")


def get_puuid(name, region):    
    region = regions.region_converter_fullname(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    return summoner.json().get("puuid")

