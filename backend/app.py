from flask import Flask, jsonify
from flask_cors import CORS

from handle_places import get_PLACES_data_float, get_hue_from_feature_data, build_feature_layer_object

app = Flask(__name__)
CORS(app)

@app.route('/cancer-layer')
def get_cancer_data():
    feature_string = "CANCER_CrudePrev"
    places_points = get_PLACES_data_float(feature_string)
    points_with_hue = get_hue_from_feature_data(places_points)
    features_object = build_feature_layer_object(points_with_hue)
    return jsonify(features_object)

@app.route('/asthma-layer')
def get_asthma_data():
    feature_string = "CASTHMA_CrudePrev"
    places_points = get_PLACES_data_float(feature_string)
    points_with_hue = get_hue_from_feature_data(places_points)
    features_object = build_feature_layer_object(points_with_hue)
    return jsonify(features_object)

if __name__ == "__main__":
    app.run(debug=True)