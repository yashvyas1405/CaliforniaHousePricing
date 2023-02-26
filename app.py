import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')   ## first route/page 
def home():
    return render_template('home.html')

## Api creation which we can call through postman.(send a request to app and get output)
@app.route('/predict_api', methods = ['POST'])
def predict_api():
    ## Get DATA
    data = request.json['data']   ##whenever i hit predict_api the input will be in json format
    print(data)

    ## Standard Scalar
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))

    ## Model
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)