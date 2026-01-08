# 🏏 T20I Cricket Prediction WebApp – User Guide

This guide explains how to run the **T20I Cricket Match Prediction Web Application** on your local machine.

---

## 📊 Dataset Source

**All T20 Internationals Dataset (2005–2023)**  
🔗 https://www.kaggle.com/datasets/bhuvaneshprasad/all-t20-internationals-dataset-2005-to-2023

---

## 🔧 Requirements

Ensure you have:
- Python 3.9 or newer
- A web browser (Chrome, Edge, Firefox)

---

## 📦 Required Files

Make sure the following files are present in the same folder:
- app.py
- match_winner_model.pkl
- safe_score_model.pkl
- toss_decision_model.pkl
- team_strength.json
- venue_encoding.json

---

## 📥 Install Required Libraries

Open Command Prompt / PowerShell in this folder and run:
```bash
pip install streamlit scikit-learn pandas numpy joblib
```

## ▶️ Run the Web Application

From the same directory, execute:
```bash
python -m streamlit run app.py (windows)
```

## 🌐 Access the App

Once the command runs, the browser should open automatically.
If not, open a browser manually and visit:

http://localhost:8501

---

## 🧭 How to Use the App

- Select Team 1
- Select Team 2 
- Select Venue Stadium

Click Predict Match

The app will display:
- 🪙 Best Toss Decision
- 🏏 Safe First Innings Score
- 🏆 Predicted Match Winner
- 📊 Prediction Confidence

---

## ⚠️ Notes

Predictions are probabilistic, not guaranteed
Accuracy is higher for frequently played teams and venues
Unseen teams or venues are handled using average historical values

---

## 📄 Disclaimer

This application is intended for educational and academic purposes only.
It should not be used for betting or financial decision-making.
