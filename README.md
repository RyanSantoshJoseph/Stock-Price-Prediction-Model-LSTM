# Stock Price Predictor

A minimal web app to predict stock prices using an LSTM model — powered by TensorFlow and Gradio, with a clean, glassmorphism-inspired interface.

[Live Demo →](https://huggingface.co/spaces/RyanJoseph40/PricePredictionModelLSTM)

---

### Features

- 📊 Predict future stock prices from sequences of past features
- 🧠 Uses a trained LSTM model
- 🌐 Web app built with Gradio
- 💎 Modern glass UI with smooth hover interactions

---
###  About

This project was developed as part of a **Data Analyst Internship at Zidio**, collaboratively built by a team of interns to explore time-series forecasting using deep learning models.
---
### Example Inputs

Provide a comma-separated list of normalized stock features:
0.12, 0.15, 0.17, 0.19, 0.22
0.30, 0.32, 0.33, 0.31, 0.34
0.50, 0.49, 0.47, 0.46, 0.45


---

### Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install gradio tensorflow numpy
```
Run locally:
```bash
python app.py

```

