import regions
import requests

def get_past_matches(name, region, number_of_matches):
    print(number_of_matches)
    region = regions.region_converter_web(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
