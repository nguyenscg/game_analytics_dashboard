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

@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, players=data)

if __name__ == "__main__":
    app.run(debug=True)