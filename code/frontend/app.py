from flask import Flask, render_template, request
import tensorflow as tf
keras = tf.keras
from keras import models
import numpy as np

app = Flask(__name__)
# Load your pre-trained machine learning model here
model = models.load_model("models/ann_best_model.keras")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input from the form
        age = request.form.get("age")
        sex = request.form.get("sex")
        cp = request.form.get("cp")
        trestbps = request.form.get("trestbps")
        chol = request.form.get("chol")
        fbs = request.form.get("fbs")
        restecg = request.form.get("restecg")
        thalach = request.form.get("thalach")
        exang = request.form.get("exang")
        oldpeak = request.form.get("oldpeak")
        slope = request.form.get("slope")
        ca = request.form.get("ca")
        thal = request.form.get("thal")

        # Handle optional input
        if chol == "":
            chol = 187 # average value
        if fbs == "":
            fbs = 0 # average value
        if oldpeak == "":
            oldpeak = 0 # average value
        if slope == "":
            slope = 1
        if ca == "":
            ca = 0
        if thal == "":
            thal = 3

        # Convert all input to ints or floats
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = float(ca)
        thal = int(thal)

        # Convert the user input to a numpy array
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Preprocess the input data for your model (if needed)
        # ... your data preprocessing code here ...
        preprocessed_data = input_data
        # Make prediction using your model
        prediction: np.ndarray = model.predict([preprocessed_data])  # Assuming a list input

        # Format the prediction for display
        # Convert the probabilities to binary predictions
        binary_prediction = (prediction > 0.5).astype(int)
        predicted_class = binary_prediction[0]  # Assuming single class output
        predicted_class = "Heart Disease" if predicted_class == 1 else "No Heart Disease"

        return render_template("result.html", prediction=predicted_class)

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
