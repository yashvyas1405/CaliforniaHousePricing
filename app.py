import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')   ## first route/page 
@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/work.html')   ## first route/page
def work():
    return render_template('work.html')

@app.route('/about.html')   ## first route/page
def about():
    return render_template('about.html')

## Api creation which we can call through postman.(send a request to app and get output)
# @app.route('/predict_api', methods = ['POST'])
# def predict_api():
#     ## Get DATA
#     data = request.json['data']   ##whenever i hit predict_api the input will be in json format
#     print(data)

#     ## Standard Scalar
#     print(np.array(list(data.values())).reshape(1, -1))
#     new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))

#     ## Model
#     output = regmodel.predict(new_data)
#     print(output[0])
#     return jsonify(output[0])

@app.route('/work.html', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    
    return render_template("work.html", prediction_text = "The house price in California will be : {}".format(output))

# @app.route('/predict', methods=['POST'])
# def predict():
#     form_data = request.form
#     values = ', '.join(form_data.values())
#     return f"Form submitted successfully! Values: {values}"

if __name__ == "__main__":
    app.run(debug=True)