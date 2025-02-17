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

# first we load the data.. now  we create a function to 'search' for a player based on gameName and tagLine
# search function with take the user's input of gameName and tagLine.. search for the player in the database
def search_player(data, username, tag):
    # loop through data file to see if a player exists
    for player in data:
        if player['gameName'].lower() == username.lower() and player['tagLine'].lower() == tag.lower():
            # returns details of player if found
            print(f"===== Stats for {player['gameName']}#{player['tagLine']} =====\n"
                  f"Average Kills: {player['average_kills']}\n"
                  f"Average Deaths: {player['average_deaths']}\n"
                  f"Win Rate: {player['win_rate']}%\n"
                  f"Total Matches: {player['total_matches']}\n"
                  f"Most Played Agent: {player['most_played_agent']}\n")
            return player
    # return None if player is not found (no value)
    print(f"{username}#{tag} not found!")
    return None

def create_player():
    # Prompt the user for all necessary information
    game_name = input("Enter player's game name: ").strip()
    while not game_name:
        game_name = input("Game name cannot be empty. Enter player's game name: ").strip()
    
    tag_line = input("Enter player's tag line: ").strip()
    while not tag_line:
        tag_line = input("Tag line cannot be empty. Enter player's tag line: ").strip()

    avg_kills = input("Enter average kills: ").strip()
    while not avg_kills.isdigit():
        avg_kills = input("Please enter a valid number for average kills: ").strip()
    avg_kills = int(avg_kills)

    avg_deaths = input("Enter average deaths: ").strip()
    while not avg_deaths.isdigit():
        avg_deaths = input("Please enter a valid number for average deaths: ").strip()
    avg_deaths = int(avg_deaths)

    win_rate = input("Enter win rate (0-100): ").strip()
    while not win_rate.replace('.', '', 1).isdigit() or not (0 <= float(win_rate) <= 100):
        win_rate = input("Please enter a valid win rate between 0 and 100: ").strip()
    win_rate = round(float(win_rate), 2)

    total_matches = input("Enter total matches: ").strip()
    while not total_matches.isdigit():
        total_matches = input("Please enter a valid number for total matches: ").strip()
    total_matches = int(total_matches)

    most_played_agent = input("Enter most played agent: ").strip()
    while not most_played_agent:
        most_played_agent = input("Agent name cannot be empty. Enter most played agent: ").strip()

    # Create a new player dictionary
    new_player = {
        "gameName": game_name,
        "tagLine": tag_line,
        "average_kills": avg_kills,
        "average_deaths": avg_deaths,
        "win_rate": win_rate,
        "total_matches": total_matches,
        "most_played_agent": most_played_agent
    }

    # Add the new player to the data
    new_data.append(new_player)
    print(f"Player {game_name}#{tag_line} created successfully!")
    
    with open("mock_data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
    print("Changes saved to mock_data.json successfully!")

# # update a player's stats
def update_player(data, username, tag):
    # search for player, call on search function
    player = search_player(data, username, tag)

    # print error message if player not found.
    if not player:
        return data
    
    # Prompt for user to select a stat to update
    stat_to_update = input("Which stat would you like to update? (1-5): ")
    
    # set dictionary to allow user to pick an option for a stat they want to update
    current_stat = {
        "1": "average_kills",
        "2": "average_deaths",
        "3": "win_rate",
        "4": "total_matches",
        "5": "most_played_agent",
    }

    # if there's a stat that is not in the options, print an error message
    if stat_to_update not in current_stat:
        print("Invalid. Please enter a stat to update.")
        return data
    
    # get stat key from dictionary
    stat = current_stat[stat_to_update]

    # store the value the user enters
    new_stat = input(f"Enter a new value for {stat.replace("_", " ").title()}: ").strip()

    # add a confirmation for user if they are sure they want to update the stat

    # check if the stat that the user picks matches
    if stat in ['average_kills', 'average_deaths', 'total_matches']:
        # this checks if it's a number
        if not new_stat.isdigit():
            print("Invalid input. Only enter numbers.")
            return data
        new_stat = int(new_stat)
    elif stat == "win_rate":
        try:
            new_stat = round(float(new_stat), 2)
            # check if the value that the user enters is between 0 to 100, otherwise print out an error message
            if not 0 <= new_stat <= 100:
                print("Enter a number between 0 to 100.")
                return data
        except ValueError:
            print("Invalid input. Enter a valid number.")
            return data
        if not round(float(new_stat), 2):
            print("Please enter 0 to 100.")
            return data
    elif stat == "most_played_agent":
        if not new_stat.strip():
            print("Agent name cannot be empty.")
            return data
    else:
        print("Invalid input. Please try again.")
        return data

    # update the stat
    player[stat] = new_stat
    print(f"{stat.replace("_", ' ').title()} has been updated to {new_stat}.")
    
    # save changes to file
    with open("mock_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    print("Changes saved successfully!")

    return data

# Delete Function
def delete_player(data, username, tag):
    # search for a player (call on search function)
    player = search_player(data, username, tag)
    if not player:
        print(f"{username}#{tag} not found!")
        return data
    
    # Prompt for user if they want to delete username#tag, Confirm deletion, print cancelled if user says no
    confirm = input(f"Are you sure you want to delete {player['gameName']}#{player['tagLine']}? (Yes/No): ").lower()
    if confirm == "yes":
        data.remove(player)
        print(f"{player['gameName']}#{player['tagLine']} has been removed.")
    else:
        print("Deletion cancelled.")
        return data
    
    # save changes
    with open("mock_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
        print("Changes saved successfully!")
    return data

# # create a main menu function to give users the options on CRUD
def main_menu(data):
    # add while loop so it re-prompts the menu screen until user picks option 4 to exit
    while True:
        # Display a list of options for the user
        print("[=======Game Analytics Dashboard======]")
        print("1. View Player Stats")
        print("2. Create Player")
        print("3. Update Player Stats")
        print("4. Delete Player")
        print("5. Exit")
        # Prompt user to get input of what option they want
        choice = input("Which would you like to do? (1-4): ").strip()
        
        # Call on function based on user's choice
        # choice 1 should call on the search_player function
        if choice == "1":
            username = input("Enter a username: ").strip()
            while not username:
                username = input("Enter a username. Field cannot be empty. ").strip() 
            tag = input("Enter a tag: ").strip()
            while not tag:
                tag = input("Enter a tag. Field cannot be empty. ").strip()
            search_player(data, username, tag)
        # choice 2 should call on create_player function
        elif choice == "2":
            create_player()
        # choice 3 should call on the update_player function
        elif choice == "3":
            username = input("Enter a username: ").strip()
            tag = input("Enter a tag: ").strip()
            update_player(data, username, tag)
        # choice 4 should call on the delete_player function
        elif choice == "4":
            username = input("Enter a username: ").strip()
            tag = input("Enter a tag: ").strip()
            delete_player(data, username, tag)
        # choice 5 should exit the program
        elif choice == "5":
            print("Exiting.. See you later!")
            break
        # else should print an error statement. If choice is invalid.
        else:
            print("Invalid choice. Pick a number between 1 to 4.")
main_menu(data)