
from flask import Flask, request,jsonify
import pickle
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask('lifeexp')
model = pickle.load( open('model_fromscratch.pkl', 'rb') )
scaler = pickle.load( open('scaling.pkl', 'rb') )

@app.route('/predict', methods=['POST'])
def predict():
    data_as_dic=request.get_json()
    data_as_array = np.array(list(data_as_dic.values())).reshape(1,-1)
    print('Data shape:', data_as_array.shape)
    print('Data shape:', data_as_array.shape)
    data_sc=scaler.transform(data_as_array)
    output=model.predict(data_sc)
    print('Predicted value:', output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
