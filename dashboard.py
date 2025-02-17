from flask import Flask, render_template, request, send_from_directory
import datetime
import json
import os

app = Flask(__name__)

# read mock_data.json
try:
    with open ("mock_data.json", "r") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    data = []
    print("Error: mock_data.json file not found.")

# home route
@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, players=data)

@app.route('/riot.txt')
def get_riot_txt():
    return send_from_directory(os.getcwd(), 'riot.txt')

# add a search route that allows the user to 'search' for a player and display their stats
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        player_name = request.form.get("username", "").strip().lower()
        player_tag = request.form.get("tag", "").strip().lower()
        found_player = None
        for player in data:
            if player_name == player['gameName'].lower() and player_tag == player['tagLine'].lower():
                found_player = player
                break
        return render_template("search_results.html", username=player_name, tag=player_tag, results=found_player)
    return render_template("search.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)