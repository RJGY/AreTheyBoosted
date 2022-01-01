from decouple import config

def get_key():
    return config('TOKEN')