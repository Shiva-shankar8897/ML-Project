# 🏠 House Price Prediction Web App

A Machine Learning + Flask web application that predicts house prices based on property features and location.
This project demonstrates end-to-end ML workflow including data preprocessing, model training, backend integration, and frontend visualization.

---

## 🚀 Features

* 🧠 Machine Learning price prediction (Linear Regression)
* 🌍 Map-based location picker (Leaflet.js)
* 📊 Price visualization chart (Chart.js)
* 🧭 Responsive Navbar with logo
* 📱 Mobile-friendly UI design
* 🌐 Flask web deployment ready

---

## 📂 Project Structure

house-price-ml-flask/
│
├── app.py
│
├── data/
│   └── house_data.csv
│
├── models/
│   ├── model.pkl
│   └── place_encoder.pkl
│
├── src/
│   └── train.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── logo.png
│
├── requirements.txt
└── README.md

---

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression

**Input Features:**

* Area (sq ft)
* Bedrooms
* Bathrooms
* Age of house
* Location (encoded)

**Libraries Used:**

* Pandas
* NumPy
* Scikit-learn

---

## 🌍 Map Integration

Users select property location via an interactive map powered by:

* Leaflet.js
* OpenStreetMap tiles

Latitude and Longitude are captured for prediction input.

---

## 📊 Visualization

Prediction results are displayed using:

* Chart.js bar graph
* Real-time predicted price display

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/yourusername/house-price-ml-flask.git
cd house-price-ml-flask

---

### 2️⃣ Create Virtual Environment (Optional)

python -m venv venv
venv\Scripts\activate   (Windows)

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Train Model

cd src
python train.py

This generates:

models/model.pkl
models/place_encoder.pkl

---

### 5️⃣ Run Flask App

cd ..
python app.py

Open in browser:

http://127.0.0.1:5000

---

## 🖥️ UI Highlights

* Gradient modern background
* Card-style responsive layout
* Navigation bar with branding
* Interactive location map
* Prediction chart visualization

---

## 📦 Requirements

flask
pandas
numpy
scikit-learn

Install all:

pip install -r requirements.txt

---

## 🧪 Future Enhancements

* Advanced ML models (Random Forest, XGBoost)
* City-wise price heatmaps
* Prediction history database
* User authentication system
* Cloud deployment (AWS / Render)
* PDF prediction reports

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/Shiva-shankar8897

---

⭐ If you like this project, give it a star on GitHub!
