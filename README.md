# AgriP — Crop Intelligence Web App 🌿

AgriP is a Flask-based web application that helps farmers make smarter decisions about their crops. It was built and deployed on [Render](https://render.com), so it can be accessed from any browser without installing anything.

---

## What It Does

### 🏠 Home
A clean landing page that introduces the platform and guides users to the available tools.

### 💰 Crop Price Prediction
Enter the crop name and your region — the app predicts the expected market price using a trained machine learning model. Useful for planning when and where to sell.

### 🌾 Crop Recommendation
Tell the app your region, soil type, and land area — it recommends which crops are best suited for your situation. Takes the guesswork out of crop selection.

### 🛒 Marketplace
Browse live marketplace data showing what buyers are looking for, current demand trends, and available listings.

---

## Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/) — Python web framework
- **Machine Learning**: scikit-learn (Linear Regression for prices, Random Forest for recommendations)
- **Templates**: Jinja2 HTML templates with custom CSS
- **Deployment**: Render (see `render.yaml` for config)
- **Language**: Python

---

## How to Run It Locally

**1. Clone the repo**
```bash
git clone https://github.com/RISHI-1575/agrip1.git
cd agrip1
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the app**
```bash
python app.py
```

Open your browser at `http://localhost:5000`

---

## Deploying to Render

This project includes a `render.yaml` file, which means you can deploy it to Render with one click.

1. Push this repo to GitHub
2. Connect it to [Render](https://render.com)
3. Render picks up the config automatically and deploys it

---

## Project Structure

```
agrip1/
├── app.py                        # Flask routes and app entry point
├── config.py                     # App configuration
├── render.yaml                   # Render deployment config
├── requirements.txt
├── data/
│   ├── market_demand.csv
│   ├── price_data.csv
│   └── soil_data.csv
├── models/
│   ├── crop_price_model.pkl      # Trained price prediction model
│   ├── crop_recommendation.pkl   # Trained crop recommendation model
│   ├── generate_crop_price_model.py
│   ├── generate_crop_recommendation_model.py
│   └── preprocess.py
├── utils/
│   ├── marketplace.py
│   ├── prediction.py
│   └── recommendation.py
└── templates/
    ├── home.html
    ├── crop_price.html
    ├── crop_recommendation.html
    └── marketplace.html
```
