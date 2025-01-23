# Game Analytics Dashboard
# Python based project that will showcase a player's statistics, match history, and win-rate


# Player overview: This will display the player's data
# Player Data should have puuid (just an id #), gameName, tagLine, average_kills, average_deaths, win_rate %, total_matches, and most_played_agent

# Start with creating a mock_data.json, will sign up for production key later for Riot API

# first import json library
import json

# data to create mock_data.json with
new_data = [
    {
        "puuid": "12345",
        "gameName": "Soli",
        "tagLine": "awice",
        "average_kills": 18,
        "average_deaths": 10,
        "win_rate": 66.67,
        "total_matches": 132,
        "most_played_agent": "Jett"
    }
]

# load the player data
def load_player_data():
    # error handling
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
        return new_data
data = load_player_data()
print(data)

# first we load the data.. now  we create a function to 'search' for a player based on gameName and tagLine
# search function with take the user's input of gameName and tagLine.. search for the player in the database
def search_player(data, username, tag):
    for player in data:
        if player["gameName"].lower() == username.lower() and player["tagLine"].lower() == tag.lower():
            return player
# get user's input to enter the gameName and tagLine || add strip() method to ensure there's no whitespace when the user enters the name and tag
player_name = input("Enter username: ").strip()
while not player_name:
    player_name = input("Username cannot be empty. Please enter username: ").strip()
player_tag = input("Enter tag: ").strip()
while not player_tag:
    player_tag = input("Tag cannot be empty. Please enter a tag: ").strip()

player = search_player(data, player_name, player_tag)

if player:
    print(f"{player['gameName']}#{player['tagLine']}'s Stats:\n"
          f"Average Kills: {player['average_kills']}\n"
          f"Average Deaths: {player['average_deaths']}\n"
          f"Win rate: {player['win_rate']}%\n"
          f"Total Matches: {player['total_matches']}\n"
          f"Most Played Agent: {player['most_played_agent']}")
else:
    print(f"Player {player_name}#{player_tag} cannot be found.")

# update a player's stats
def update_player(data, username, tag):
    # search for player
    player = search_player(data, player_name, player_tag)
    if not player:
        print(f"Player {player_name}#{player_tag} does not exist")

    print(f"Current Stats for {player_name}#{player_tag}\n"
          f"Average Kills: {player["average_kills"]}"
          f"Average Deaths: {player["average_deaths"]}"
          f"Win Rate: {player["win_rate"]}"
          f"Total Matches: {player["total_matches"]}"
          f"Most Played Agent: {player["most_played_agent"]}")
    # Prompt for user to select a stat to update
    stat_to_update = input("Which stat would you like to update?")
    current_stat = {
        "1": "average_kills",
        "2": "average_deaths",
        "3": "win_rate",
        "4": "total_matches",
        "5": "most_played_agent",
    }

    if stat_to_update not in current_stat:
        print("Invalid. Please enter a stat to update.")
        return data

    stat = current_stat[stat_to_update]
    new_stat = input(f"Enter a new value for {stat}: ").strip()

    if stat in ['average_kills', 'average_deaths', 'win_rate', 'total_matches', 'most_played_agent']:
        if not new_stat.isdigit():
            print("Invalid input. Only numeric values.")
            return data
        new_stat = int(new_stat) if stat != "win_rate" else float(new_stat)

    player[stat] = new_stat
    print(f"{stat} has been updated to {new_stat}.")

    # save changes to file
    with open("mock_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    print("Changes saved successfully!")

    return data

data = update_player(data, player_name, player_tag)

# Delete Function
def delete_player(data, username, tag):
    # search for player


    # confirm delete

    # delete player
    
    # save changes

    # feedback -- success message that the deletion was successful