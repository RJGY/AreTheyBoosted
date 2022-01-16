import api_request as api
import requests
import regions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_rank(name, region):
    region = regions.region_converter_fullname(region)
    summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(region, name), headers=api.summoner_request_headers())
    summoner_rank = requests.get("https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(region, summoner.json().get("id")), headers=api.summoner_request_headers())
    for rank_type in summoner_rank.json():
        if rank_type.get("queueType") == "RANKED_SOLO_5x5":
            return "{} {} {} LP".format(rank_type.get("tier"), rank_type.get("rank"), rank_type.get("leaguePoints"))

def get_previous_ranks(name, region):
    region = regions.region_converter_web(region)
    print(region)
    # start in headless
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    # get with selenium
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    # get opgg
    driver.get("https://{}.op.gg/summoner/userName={}".format(region, name))
    # refresh page
    driver.find_element(By.ID, 'SummonerRefreshButton').click()
    # get top elements
    rank_class = driver.find_element(By.CLASS_NAME, 'PastRankList')
    rank_list = rank_class.find_elements_by_tag_name("li")
    for x in rank_list:
        print(x.text)
    

get_previous_ranks("Reese", "Oceania")