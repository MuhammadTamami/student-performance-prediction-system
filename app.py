from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load best model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "Student Performance Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        features = np.array([[
            data["Age"],
            data["Gender"],
            data["Ethnicity"],
            data["ParentalEducation"],
            data["StudyTimeWeekly"],
            data["Absences"],
            data["Tutoring"],
            data["ParentalSupport"],
            data["Extracurricular"],
            data["Sports"],
            data["Music"],
            data["Volunteering"]
        ]])
            
        prediction = model.predict(features)
        
        return jsonify({
            "Predict GPA ": round(float(prediction[0]), 2)
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        })
        
if __name__ == "__main__":
    app.run(debug=True)
    