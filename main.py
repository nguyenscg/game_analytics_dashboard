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
# print(data)

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
    player = search_player(data, username, tag)
    if not player:
        print(f"Player {username}#{tag} does not exist")

    print(f"Current Stats for {username}#{tag}\n"
          f"Average Kills: {player["average_kills"]}\n"
          f"Average Deaths: {player["average_deaths"]}\n"
          f"Win Rate: {player["win_rate"]}\n"
          f"Total Matches: {player["total_matches"]}\n"
          f"Most Played Agent: {player["most_played_agent"]}\n")
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

# data = update_player(data, player_name, player_tag)

# Delete Function
def delete_player(data, username, tag):
    # search for player (call on search function)
    player = search_player(data, username, tag)
    if not player:
        print(f"{username}#{tag} does not exist.")
        return data

    # confirm delete
    # prompt for user if they want to delete username#tag
    confirm = input(f"Are you sure you want to delete {username}#{tag}? (Yes/No)")
    if confirm.lower() != 'yes':
        print("Deletion cancelled.")
        return data
    
    # delete player
    data.remove(player)
    print(f"{username}#{tag} has been removed.")

    # save changes
    with open("mock_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
        print("Changes saved successfully!")
# player_name = input("Enter username: ")
# player_tag = input("Enter tag: ")

# data = delete_player(data, player_name, player_tag)
#     # feedback -- success message that the deletion was successful

# create a main menu function to give users the options on CRUD
def main_menu(data):
    # Display a list of options to user
    print("[=======Game Analytics Dashboard======]")
    print("1. View Player Stats")
    print("2. Update Player Stats")
    print("3. Delete Player")
    print("4. Exit")
    # Accept the user input of their choice
    choice = input("Which would you like to do? (1-4): ").strip()
    # Call function on user's choice
    # So choice 1 should call onto the search function to look for the player and dislpay their stats
    if choice == "1":
        username = input("Enter a username: ").strip()
        tag = input("Enter a tag: ").strip()
        player = search_player(data, username, tag)
        if player:
            print(f"===== Stats for {player['gameName']}#{player['tagLine']} =====\n"
                  f"Average Kills: {player['average_kills']}\n"
                  f"Average Deaths: {player['average_deaths']}\n"
                  f"Win Rate: {player['win_rate']}%\n"
                  f"Total Matches: {player['total_matches']}\n"
                  f"Most Played Agent: {player['most_played_agent']}")
        else:
            print(f"{username}#{tag} not found.")
    elif choice == "2":
        username = input("Enter a username: ").strip()
        tag = input("Enter a tag: ").strip()
        data = update_player(data, username, tag)
    elif choice == "3":
        username = input("Enter a username: ").strip()
        tag = input("Enter a tag: ").strip()
        data = delete_player(data, username, tag)
    elif choice == "4":
        print("Exiting.. See you later!")
    # choice 2 should call onto the update_player function
    # choice 3 should call onto delete_player function
    # choice 4 should exit
    # Allow users to exit menu
    return data
main_menu(data)