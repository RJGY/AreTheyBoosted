from api import get_rank

class Player:
    def __init__(self, name=None, region=None):
        self.name = name
        self.region = region
        self.get_rank()

    def get_rank(self):
        if self.name is None:
            return None
        try: 
            player_api = get_rank.get_rank(self.name, self.region)
        except Exception as ex:
            print(ex)
        print(player_api.ranks)

dude = Player('Reese', 'Oceania')
