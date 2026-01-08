# 🏏 T20I Cricket Match Prediction WebApp

An end-to-end machine learning project that predicts:
- 🪙 Best toss decision (Bat / Bowl)
- 🏏 Safe first-innings score
- 🏆 Match winner with confidence

using historical T20 International cricket data.

This project focuses on **practical sports analytics**, feature engineering, and real-world ML deployment via a web application.

---

## 📊 Dataset

This project uses the following public dataset from Kaggle:

**All T20 Internationals Dataset (2005–2023)**  
🔗 https://www.kaggle.com/datasets/bhuvaneshprasad/all-t20-internationals-dataset-2005-to-2023

The dataset includes detailed match-level information such as teams, venues, toss results, scores, and match outcomes.

---

## 🚀 Features

- Match winner prediction using team strength & venue behavior
- Toss decision recommendation based on historical success
- Safe first-innings score estimation
- Probability-based predictions (not rule-based)
- Interactive web UI built with **Streamlit**
- Clean ML pipeline with saved models and encodings

---

## 🧠 Machine Learning Approach

### Key Techniques Used
- Target encoding for team strength (win percentage–based)
- Venue behavior encoding (bat-first bias & match density)
- Feature engineering (strength difference, toss impact)
- Ensemble learning with **Random Forest**
- Separate models for:
  - Match winner (classification)
  - Toss decision (classification)
  - Safe score (regression)

### Why Random Forest?
- Works well on tabular sports data
- Handles non-linear relationships
- Robust against noise and imbalance

---

## 📊 Model Performance (Approx.)

| Task | Metric | Result |
|----|----|----|
Match Winner | Accuracy | ~60–65%
Toss Decision | Accuracy | ~60–70%
Safe Score | MAE | ~10–18 runs

> Note: Cricket is a probabilistic sport. These results are realistic for pre-match predictions.

---

## 🖥️ Web Application

The project includes a **Streamlit-based web application** with dropdown menus for:
- Team 1
- Team 2
- Venue Stadium

The app outputs:
- Best toss decision
- Safe first-innings score
- Predicted match winner
- Prediction confidence

---

## 🎓 Academic Context

This project was completed as a **Year 2 Semester 1 group project** for a university module related to Artificial Intelligence / Machine Learning.

---

## 👥 Group Members

- **Kasun Akalanka**
- **Pramuditha Jayamuthu**
- **Dananjaya Atapattu**
- **Yenuli Thevinya**
- **Yethmi Peiris**

---

## ⚠️ Disclaimer

This tool is developed for **educational and analytical purposes only**.  
Predictions are based on historical data and do not guarantee real match outcomes.

---

## 🙌 Author (Repository Owner)

**Kasun Akalanka**  
🔗 Portfolio: https://kasun-akalanka-web.vercel.app
