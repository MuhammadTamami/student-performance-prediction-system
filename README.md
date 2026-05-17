# Student Performance Prediction System

## Project Overview

This project is a Machine Learning-based Student Performance Prediction System designed to predict student GPA using academic and behavioral factors such as study time, absences, parental support, tutoring, extracurricular activities, and more.

The project includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Multiple Model Training
- Model Comparison
- Best Model Selection
- Model Deployment using Flask API

This project was built as part of an AI Engineer portfolio project.

---

## Dataset Information

Dataset contains:

- Student demographics
- Academic habits
- Attendance records
- Family support indicators
- Extracurricular participation
- Final GPA (Target Variable)

Total Data:

- 2392 rows
- 15 columns

Target:

```python
GPA

Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
XGBoost
Flask
Pickle
Jupyter Notebook
------

Machine Learning Models Used
1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor
Model Performance Comparison
Model	MAE	RMSE	R² Score
Linear Regression	0.155	0.196	0.953
Random Forest	0.191	0.246	0.927
XGBoost	0.173	0.219	0.942

Best Model
Linear Regression

Linear Regression outperformed Random Forest and XGBoost due to the strong linear relationship between student absences and GPA.

Best Result:

R² Score = 0.953
API Deployment

This project includes Flask API deployment for real-time GPA prediction.

Endpoint
POST /predict
Example JSON Input
{
    "Age": 20,
    "Gender": 1,
    "Ethnicity": 2,
    "ParentalEducation": 3,
    "StudyTimeWeekly": 15,
    "Absences": 5,
    "Tutoring": 1,
    "ParentalSupport": 4,
    "Extracurricular": 1,
    "Sports": 1,
    "Music": 0,
    "Volunteering": 1
}

Example Output
{
    "Predict GPA": 3.67
}

How to Run
- Install Dependencies
- pip install -r requirements.txt
- Run Flask API
- python app.py

Future Improvements
- Frontend Dashboard
- User Authentication
- Docker Deployment
- FastAPI Migration
- Cloud Deployment (AWS/GCP)

Author
Muhammad Tamami