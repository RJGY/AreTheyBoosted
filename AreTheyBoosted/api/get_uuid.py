import regions
import requests
import api_request as api

# TODO: Error handling for wrong name or region

def get_uuid(name=None, region=None):
    if name is None or region is None:
        print("Default values not accepted.")
    region = regions.region_converter_fullname(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    return summoner.json().get("id")


def get_puuid(name=None, region=None):
    if name is None or region is None:
        print("Default values not accepted.")    
    region = regions.region_converter_fullname(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    return summoner.json().get("puuid")

