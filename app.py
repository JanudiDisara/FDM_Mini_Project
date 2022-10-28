import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('ML_Models/model.pkl', 'rb'))
#model2 = pickle.load(open('ML_Models/rfc_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    #prediction2 = model2.predict(final_features)

    output = round(prediction[0])
    #output2 = prediction2[0]

    return render_template('index.html', prediction_text='Is  Cancelled is (Logistic)--- {} '.format(output))


if __name__ == "__main__":
    app.run(debug=True)