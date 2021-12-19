# AreTheyBoosted 
Is the your/enemy team boosted. The answer is always yes. But with this, you can actually make sure they are boosted.

# TODO
* LOGGER CAUSE WE NEED IT
* API connectivity to main league api + opggs one if thats possible
* Flask for the web app
* Boosted detection algo
* MAKE SURE U ACTUALLY FIND BOOSTED ACCS AND RUN THE NUMBERS SO THAT THE ALGO IS SOMEWHAT CORRECT NOT JUST COMPLETE BULLSHIT
* Input
* UI
more later idk ill think of more stuff to do

# Detection algo
* Summoner spell swapping
* Role swapping & champ swapping & winning
* Swapping champions in role/offrole champion swapping
* Winstreak with duo thats more than 5 games
* Playing at different times of the day
* Win streaking solo more than 5 games in a row
* OPGG MVP score greater than average over past 5 games
* KDA & ward score
* Rank over the course of the season based on past 20 games
* Current rank vs previous seasons

Algo should take all into account however different ones weigh more or less. e.g summoner spell swapping is a high liklihood of account sharing/boosting so should have a higher weighting compared to a solo 5 game winstreak which could just be a lucky day for the player. It is more likely that someone is being boosted if they summoner swap than if they win 5 times in a row. 

Weighting will work like this. 
# Weighting
* 0 to 30 - Not boosting/acc sharing
* 31 to 65 - Possibly boost/acc sharing
* 65 to 100 - Most likely boosting/acc sharing
* 100+ - Nearly certainly boosting/acc sharing

# Scoring
* Summoner Spell Swapping - 70
* Recent Role Swapping w/ Games > 10 - +1 point for every %WR above 60%
* Swapping Champion in role w/ Games >= 10 - +1 point for every %WR above 60%
* Winstreak with duo over 5 games - 20 points
* Playing at different times of day - 5 points
* Winstreak solo over 5 games - 10 points
* MVP/Ace score on 5 or more games in past 10 games - 10 points
* KDA/Ward score higher than tier average - 5 points
* High rank over the course of the season based on past 20 games - 10 points
* Current rank vs previous season ranks - 5 points

# ACTIVATE FLASK TO RUN IT WITH THIS
* venv\Scripts\activate
* 