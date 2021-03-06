import api_request as api
import requests
import regions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# TODO: create error handling for incorrect names and region
# TODO: bug where if u reload opgg profile too quickly, could come up with "Oooops! You just updated it 22 seconds ago, try again in 98 seconds!" alert box.
# TODO: custom exception class????
def get_rank(name=None, region=None):
    if name is None or region is None:
        raise Exception("Default values are not accepted. Exiting")
    try:
        region = regions.region_converter_fullname(region)
    except Exception:
        raise Exception("Incorrect region. Exiting")
    try: 
        summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    except Exception:
        raise Exception("Incorrect status code. Exiting")
    try:
        summoner_rank = requests.get("https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(region, summoner.json().get("id")), headers=api.summoner_request_headers())
    except Exception:
        print("get_rank: Wrong status code for summoner_rank request.")
    for rank_type in summoner_rank.json():
        if rank_type.get("queueType") == "RANKED_SOLO_5x5":
            return "{} {} {} LP".format(rank_type.get("tier"), rank_type.get("rank"), rank_type.get("leaguePoints"))


def get_previous_ranks(name=None, region=None):
    if name is None or region is None:
        return
    try:
        region = regions.region_converter_web(region)
    except Exception:
        print("Region is incorrect")
        return
    # start in headless
    options = Options().add_argument("--headless").add_argument("--window-size=1920x1080")
    # get with selenium
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        # get opgg
        driver.get("https://{}.op.gg/summoner/userName={}".format(region, name))
        # refresh page
        try:
            driver.find_element(By.ID, 'SummonerRefreshButton').click()
        except:
            print("ok its fucked")
            return
        # get top elements
        rank_class = driver.find_element(By.CLASS_NAME, 'PastRankList')
        rank_list = rank_class.find_elements_by_tag_name("li")
        previous_ranks = []
        for x in rank_list:
            previous_ranks.append(x.text)
        return previous_ranks
    except Exception:
        print("get_previous_ranks: Something happened in Selenium.")
        return
