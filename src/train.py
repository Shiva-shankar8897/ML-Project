import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("../data/house_data.csv")

# Encode place column
le = LabelEncoder()
df["place"] = le.fit_transform(df["place"])

# Features & target
X = df[["area", "bedrooms", "bathrooms", "age", "place"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("../models/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoder
with open("../models/place_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model & encoder saved")
