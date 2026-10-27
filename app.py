from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from helpers.helper import ohe, preprocess_input


app = Flask(__name__)
model = joblib.load("models/model.pkl")


@app.route('/')  # http://localhost:5000/
def index():
    cities = ohe.categories_[0].tolist() # [Cairo, Alexandra, Giza, Mansoura]
    return render_template('index.html', cities=cities)

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    data = request.get_json()
    df = pd.DataFrame([data])
    df_processed = preprocess_input(df)
    prediction = model.predict(df_processed) # 368,915.182
    return jsonify({'predicted_price': float(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)