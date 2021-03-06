from decouple import config


def get_key():
    return config('TOKEN')


def summoner_request_headers():
    return {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept-Language" : "en-US,en;q=0.9",
        "Accept-Charset" : "application/x-www-form-urlencoded; charset=UTF=8",
        "X-Riot-Token" : get_key()
    }