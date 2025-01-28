from flask import Flask, render_template
import datetime
import json

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

# add a search route that allows the user to 'search' for a player and display their stats
@app.route("/search")
def search():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)