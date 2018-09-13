from flask import Flask, abort, render_template, jsonify, request
from taxi_api import make_prediction

app = Flask('TimeIsMoney')

@app.route('/predict', methods=['POST'])
def gen_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = make_prediction(data)

    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
