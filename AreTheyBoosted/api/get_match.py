import re
import regions
import requests
import api_request as api
import get_uuid 

def get_past_matches(name, region, number_of_matches):
    summoner = get_uuid.get_puuid(name, region)
    return requests.get("https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?type=ranked&start=0&count={}".format(regions.region_converter_match(region), summoner, number_of_matches), headers=api.summoner_request_headers()).json()
    

print(get_past_matches('Reese', 'Oceania', '20'))