
from urllib import response
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/home')
def hello():
    return "hi"

@app.route('/predict_price', methods=['POST'])
def predict_price():
    bhk = request.form['bhk']
    bathrooms = float(request.form['bathrooms'])
    balcony = request.form['balcony']
    area = request.form['area']
    response = jsonify({"Predicted_Price":util.predict_price(bhk, bathrooms, balcony, area)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/locations')
def get_locations():
    response =  jsonify({'locations': util.get_locations()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    app.run()