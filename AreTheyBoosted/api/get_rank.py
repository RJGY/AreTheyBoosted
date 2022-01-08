import api_request as api
import requests
import regions

def get_rank(name, region):
    region = regions.region_converter(region)
    response = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    rank = requests.get("https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(region, response.json().get("id")), headers=api.summoner_request_headers())
    for rank_type in rank.json():
        if rank_type.get("queueType") == "RANKED_SOLO_5x5":
            return "{} {} {} LP".format(rank_type.get("tier"), rank_type.get("rank"), rank_type.get("leaguePoints"))

def get_previous_ranks(name, region):
    region = regions.region_converter(region)
