from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("../model/ipl_win_predictor.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "🏏 IPL Win Predictor API is Running!"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        batting_team = data["batting_team"]
        bowling_team = data["bowling_team"]
        city = data["city"]

        target = float(data["target"])
        runs_left = float(data["runs_left"])
        balls_left = float(data["balls_left"])
        wickets_left = float(data["wickets_left"])
        crr = float(data["crr"])
        rrr = float(data["rrr"])

        input_df = pd.DataFrame([{
            "batting_team": batting_team,
            "bowling_team": bowling_team,
            "city": city,
            "runs_left": runs_left,
            "balls_left": balls_left,
            "wickets_left": wickets_left,
            "target": target,
            "crr": crr,
            "rrr": rrr
        }])

        probability = model.predict_proba(input_df)[0]

        batting_win = round(float(probability[1] * 100), 2)
        bowling_win = round(float(probability[0] * 100), 2)

        return jsonify({
            "success": True,
            "batting_team_win": batting_win,
            "bowling_team_win": bowling_win
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)