# Game Analytics Dashboard
# Python based project that will showcase a player's statistics, match history, and win-rate


# Player overview: This will display the player's data
# Player Data should have puuid (just an id #), gameName, tagLine, average_kills, average_deaths, win_rate %, total_matches, and most_played_agent

# Start with creating a mock_data.json, will sign up for production key later for Riot API

# first import json library
import json

# create mock_data into .json
new_data = [
    {
        "puuid": "12345",
        "gameName": "Soli",
        "tagLine": "awice",
        "average_kills": 18,
        "average_deaths": 10,
        "win_rate": 66.67,
        "total_matches": 132,
        "most_played_agents": "Jett",
    }
]

# save/create the new data into a mock_data.json
with open("mock_data.json", "w") as data_file:
    json.dump(new_data, data_file)