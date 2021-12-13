import random
from decouple import config
import cassiopeia as cass

cass.set_riot_api_key(config('TOKEN'))  # This overrides the value set in your configuration/settings.

summoner = cass.get_summoner(name="Reese", region="OCE")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))

champions = cass.get_champions(region="OCE")
random_champion = random.choice(champions)
print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives, region="OCE")
best_na = challenger_league[0].summoner
print("He's not as good as {name} at League, but probably a better python programmer!".format(name=best_na.name))
