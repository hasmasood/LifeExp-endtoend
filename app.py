import pickle
from flask import Flask, request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import json

app = Flask(__name__)
model = pickle.load( open('model_fromscratch.pkl', 'rb') )
scaler = pickle.load( open('scaling.pkl', 'rb') )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data_as_dic=request.json['data']
    data_as_array = np.array(list(data_as_dic.values())).reshape(1,-1)
    print('Data shape:', data_as_array.shape)
    data_sc=scaler.transform(data_as_array)
    output=model.predict(data_sc)
    print('Predicted value:', output[0])
    return jsonify(output[0])

@app.route('/predict_web', methods=['POST'])
def predict():
    data_as_float = [float(x) for x in request.form.values()]
    data_as_array = np.array(data_as_float).reshape(1,-1)
    print('Data shape:', data_as_array.shape)
    data_sc=scaler.transform(data_as_array)
    output=model.predict(data_sc)
    print('Predicted value:', output[0])
    return render_template('home.html', prediction_text= "The life expentency is {}".format(output[0]))

if __name__=='__main__':
    app.run(debug=True)