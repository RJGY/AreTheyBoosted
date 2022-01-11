import api_request as api
import requests
import regions
import selenium

def get_rank(name, region):
    region = regions.region_converter(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    summoner_rank = requests.get("https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(region, summoner.json().get("id")), headers=api.summoner_request_headers())
    for rank_type in summoner_rank.json():
        if rank_type.get("queueType") == "RANKED_SOLO_5x5":
            return "{} {} {} LP".format(rank_type.get("tier"), rank_type.get("rank"), rank_type.get("leaguePoints"))

def get_previous_ranks(name, region):
    region = regions.region_converter(region)
    print(region)
    # get with selenium
    print(summoner_rank.json())


get_previous_ranks("Reese", "OCE")