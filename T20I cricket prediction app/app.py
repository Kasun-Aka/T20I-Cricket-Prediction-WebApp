import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

# ======================
# Load models
# ======================
match_winner_model = joblib.load("match_winner_model.pkl")
safe_score_model = joblib.load("safe_score_model.pkl")
toss_model = joblib.load("toss_decision_model.pkl")

# ======================
# Load encodings
# ======================
with open("team_strength.json") as f:
    team_strength = json.load(f)

with open("venue_encoding.json") as f:
    venue_data = json.load(f)

teams = sorted(team_strength.keys())
venues = sorted(venue_data["bat_bias"].keys())

# ======================
# Helper functions
# ======================
def get_team_strength(team):
    return team_strength.get(team, np.mean(list(team_strength.values())))

def get_venue_bat_bias(stadium):
    return venue_data["bat_bias"].get(stadium, 0.5)

def get_venue_density(stadium):
    return venue_data["match_density"].get(stadium, 0.5)

# ======================
# UI
# ======================
st.set_page_config(page_title="T20I Match Predictor", layout="centered")

st.title("🏏 T20I Cricket Match Prediction WebApp")
st.markdown("Predict toss decision, safe score & match winner using historical data.")

st.divider()

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", [t for t in teams if t != team1])
venue = st.selectbox("Select Venue Stadium", venues)

if st.button("🔮 Predict Match"):
    # Feature engineering
    t1_strength = get_team_strength(team1)
    t2_strength = get_team_strength(team2)
    strength_diff = t1_strength - t2_strength

    venue_bat_bias = get_venue_bat_bias(venue)
    venue_density = get_venue_density(venue)

    # Toss decision
    toss_features = pd.DataFrame([{
        "Toss Winner Strength": max(t1_strength, t2_strength),
        "Venue Bat Bias": venue_bat_bias,
        "Venue Match Density": venue_density
    }])

    toss_pred = toss_model.predict(toss_features)[0]
    toss_decision = "BAT 🏏" if toss_pred == 1 else "BOWL 🎯"

    # Safe score
    batting_team_strength = t1_strength if toss_pred == 1 else t2_strength

    score_features = pd.DataFrame([{
        "Batting Team Strength": batting_team_strength,
        "Venue Bat Bias": venue_bat_bias,
        "Venue Match Density": venue_density
    }])

    predicted_score = int(round(safe_score_model.predict(score_features)[0]))

    # Match winner
    winner_features = pd.DataFrame([{
        "Team1 Strength": t1_strength,
        "Team2 Strength": t2_strength,
        "Strength Diff": strength_diff,
        "Venue Bat Bias": venue_bat_bias,
        "Venue Match Density": venue_density,
        "Toss Bat": 1 if toss_pred == 1 else 0,
        "Toss Winner Strength": max(t1_strength, t2_strength)
    }])

    winner_pred = match_winner_model.predict(winner_features)[0]
    winner_prob = match_winner_model.predict_proba(winner_features).max()

    predicted_winner = team1 if winner_pred == 1 else team2

    # Output
    st.success("Prediction Completed")

    st.metric("🪙 Best Toss Decision", toss_decision)
    st.metric("🏏 Safe First Innings Score", f"{predicted_score} runs")
    st.metric("🏆 Predicted Match Winner", predicted_winner)
    st.metric("📊 Confidence", f"{winner_prob * 100:.1f}%")
