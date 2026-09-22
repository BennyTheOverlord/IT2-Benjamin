import json

with open("SteamSpill/games.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data["games"][0]))

least_played = 0
least_played_game = "none"
most_played = 0
most_played_game = "none"

for game in data["games"]:
    print(f" Game: {game["name"]} \n Playtime: {game["playtime_forever"]/60:.1f}")
    if game["playtime_forever"] > most_played:
        most_played = game["playtime_forever"]
        most_played_game = game["name"]

print(f"Your most played game is: {most_played_game} \n Playtime: {most_played/60:.1f} Hours")

for game in data["games"]:
    if game["playtime_forever"] < least_played and game["playtime_forever"] != 0:
        least_played = game["playtime_forever"]
        least_played_game = game["name"]
    
    elif least_played == 0:
        least_played = game["playtime_forever"]
        least_played_game = game["name"]

print(f"Your least played game is: {least_played_game} \n Playtime: {least_played/60:.1f} Hours")
    # except:
    #     if least_played = 0:
    #         least_played = game["playtime_forever"]
    #         least_played_game = game["name"]

games_played = []
games_unplayed = []

for game in data["games"]:
    if game["playtime_forever"] > 0:
        games_played.append(game["name"])

    else:
        if game["playtime_forever"] >= 0:
            games_unplayed.append(game["name"])

print(len(games_played))
#print(games_unplayed)