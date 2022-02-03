import regions
import requests
import api_request as api

# TODO: Error handling for wrong name or region

def get_uuid(name=None, region=None):
    if name is None or region is None:
        print("Default values not accepted.")
    try:
        region = regions.region_converter_fullname(region)
    except Exception:
        print("get_uuid: Incorrect Region")
    try:
        summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    except Exception:
        print("get_uuid: Something happened to the request")
    return summoner.json().get("id")


def get_puuid(name=None, region=None):
    if name is None or region is None:
        print("Default values not accepted.")
    try:    
        region = regions.region_converter_fullname(region)
    except Exception:
        print("get_puuid: Incorrect Region")
    try:
        summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    except Exception:
        print("get_puuid: Something happened to the request.")
    return summoner.json().get("puuid")

