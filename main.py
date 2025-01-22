# Game Analytics Dashboard
# Python based project that will showcase a player's statistics, match history, and win-rate


# Player overview: This will display the player's data
# Player Data should have puuid (just an id #), gameName, tagLine, average_kills, average_deaths, win_rate %, total_matches, and most_played_agent

# Start with creating a mock_data.json, will sign up for production key later for Riot API

# first import json library
import json

# load the player data
def load_player_data():
    with open("mock_data.json", "r") as data_file:
        data = json.load(data_file)
        print(data)
load_player_data()