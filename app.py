from operator import le
import os
import pickle
import numpy as np
from flask_wtf import FlaskForm
from flask import Flask, render_template
from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    data = request.form

    model_name = data["model_name"]

    if model_name == "logistic_regression":
        model = pickle.load(open('models/logistic.pkl', 'rb'))
    elif model_name == "naive_bayes":
        model = pickle.load(open('models/naive_mdl.pkl', 'rb'))
    elif model_name == "random_forest":
        model = pickle.load(open('models/rfc_model.pkl', 'rb'))
    elif model_name == "support_vector_machine":
        model = pickle.load(open('models/SVM_FDM.pkl', 'rb'))
    

    features = [data["lead_time"], data["same_room"], data["Previous_Cancellation"], data["special_requests"], data["booking_changes"]]
    final_features = [np.array([float(feature) for feature in features])]

    prediction = model.predict(final_features)

    output = round(prediction[0])

    if output == 0:
        result = "Reservation is Cancelled"
    else:
        result = "Reservation is not Cancelled"

    return render_template('index.html', prediction_text=f"{result}")

if __name__ == "__main__":
    app.run(debug=True)