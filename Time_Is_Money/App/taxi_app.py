from flask import Flask, abort, render_template, jsonify, request
from taxi_api import make_prediction
# from taxi_api import plot_the_map

app = Flask('TimeIsMoney')

@app.route('/predict', methods=['POST'])
def gen_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = make_prediction(data)

    return jsonify(response)

# @app.route('/predict', methods=['POST'])
# def plot_map():
#     if not request.json:
#         abort(400)
#     points = request.json
#
#     response = map_points(points)
#
#   return render_template('Chicago_taxi_points.html', points = [response]);

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
