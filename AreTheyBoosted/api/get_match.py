import regions
import requests
import api_request
import get_uuid 

#TODO: THROW EXCEPTION

def get_match_ids(name=None, region=None, number_of_matches=0):
    if name is None or region is None or number_of_matches == 0:
        raise Exception("Default values are not accepted. Exiting")
    summoner = get_uuid.get_puuid(name, region)
    try:
        return requests.get("https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?type=ranked&start=0&count={}".format(regions.region_converter_match(region), summoner, number_of_matches), headers=api_request.summoner_request_headers()).json()
    except Exception:
        raise Exception("Bad response. Going to die real quick.")


def get_match(matchid=None, region=None):
    if matchid is None or region is None:
        raise Exception("Default values are not accepted. Exiting")
    try: 
        return requests.get("https://{}.api.riotgames.com/lol/match/v5/matches/{}".format(regions.region_converter_match(region), matchid), headers=api_request.summoner_request_headers()).json()
    except Exception:
        raise Exception("Bad response. Going to die real quick.")


def get_matches_by_champion(name=None, region=None, champion=None):
    if champion is None or region is None or name is None:
        raise Exception("Default values are not accepted. Exiting")
    all_match_ids = get_match_ids(name, region, 50)
    all_match_list = []
    for id in all_match_ids:
        all_match_list.append(get_match(id, region))
    match_list = []
    for match in all_match_list:
        for player in match.get('info').get('participants'):
            if player.get('summonerName') == name and player.get('championName') == champion:
                match_list.append(match)
    return match_list


print(get_matches_by_champion('Submision', 'Oceania', 'Nasus'))