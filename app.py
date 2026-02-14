from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model & encoder
model = pickle.load(open("models/model.pkl", "rb"))
le = pickle.load(open("models/place_encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    age = int(request.form["age"])

    # Map lat,lng (optional use later)
    place = request.form["place"]

    import pandas as pd

    features = pd.DataFrame(
        [[area, bedrooms, bathrooms, age, 0]],
        columns=["area","bedrooms","bathrooms","age","place"]
    )

    prediction = model.predict(features)[0]

    return render_template(
        "result.html",
        prediction=f"{prediction:,.2f} Rs",
        price_value=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
