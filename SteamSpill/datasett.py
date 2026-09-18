import json

with open("SteamSpill/games.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data["games"][0]))

most_played = 0
most_played_game = "none"

for game in data["games"]:
    print(f" Game: {game["name"]} \n Playtime: {game["playtime_forever"]/60:.1f}")
    if game["playtime_forever"] > most_played:
        most_played = game["playtime_forever"]
        most_played_game = game["name"]

print(f"Your most played game is: {most_played_game} \n Playtime: {most_played/60:.1f}")
    