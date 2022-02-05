import re
import regions
import requests
import api_request as api
import get_uuid 

def get_match_ids(name=None, region=None, number_of_matches=0):
    if name is None or region is None or number_of_matches == 0:
        print("Default values are not accepted")
        return
    summoner = get_uuid.get_puuid(name, region)
    try:
        return requests.get("https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?type=ranked&start=0&count={}".format(regions.region_converter_match(region), summoner, number_of_matches), headers=api.summoner_request_headers()).json()
    except Exception:
        print("get_match_ids: Something happened with the response code.")
        return

print(get_match_ids('Reese', 'Oceania', '20'))