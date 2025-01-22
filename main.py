# Game Analytics Dashboard
# Python based project that will showcase a player's statistics, match history, and win-rate


# Player overview: This will display the player's data
# Player Data should have puuid (just an id #), gameName, tagLine, average_kills, average_deaths, win_rate %, total_matches, and most_played_agent

# Start with creating a mock_data.json, will sign up for production key later for Riot API

# first import json library
import json

new_data = [
    {
        "puuid": "67890",
        "gameName": "Solzi",
        "tagLine": "zzz",
        "average_kills": 15,
        "average_deaths": 14,
        "win_rate": 52.72,
        "total_matches": 310,
        "most_played_agent": "Omen",
    }
]

# load the player data
def load_player_data():
    try: 
        with open("mock_data.json", "r") as data_file:
            data = json.load(data_file)
            print("Loaded the data successfully!")
            return data
    except FileNotFoundError:
        print("Error. The file 'mock_data.json' was not found. Creating new file..")
        with open("mock_data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
        print("mock_data has been created successfully.")
load_player_data()