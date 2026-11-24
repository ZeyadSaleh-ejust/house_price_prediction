from flask import Flask, render_template, request, jsonify # jsonify: convert python dict to json
import joblib
import pandas as pd
from helpers.helper import ohe, preprocess_input


app = Flask(__name__)
model = joblib.load("models/model.pkl")

@app.route('/')  # http://localhost:5000/   ||| when there is a request to the endpoint '/', the function index() will be executed
def index():
    cities = ohe.categories_[0].tolist() # [Cairo, Alexandra, Giza, Mansoura]
    return render_template('index.html', cities=cities)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # convert json data to python dict
    df = pd.DataFrame([data]) # convert from dict to dataframe
    df_processed = preprocess_input(df)
    prediction = model.predict(df_processed) # ['368,915.182'] 
    return jsonify({'predicted_price': float(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)  # run the flask app in debug mode