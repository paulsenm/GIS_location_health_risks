from flask import Flask, jsonify
from flask_cors import CORS

from handle_places import get_places_oregon_test, get_PLACES_data_float, get_hue_from_feature_data, build_feature_layer_object

app = Flask(__name__)
CORS(app)

@app.route("/test")
def test_points():
    return jsonify({
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Point 1"},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-123.000, 45.000]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "Point 2"},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-123.050, 45.050]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "Point 3"},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-123.020, 45.080]
                }
            }
        ]
    })

@app.route('/oregon-test')
def oregon_test():
    return jsonify(get_places_oregon_test())

@app.route('/generic-places-data')
def get_generic_places_data():
    test_feature_string = "CANCER_CrudePrev"
    test_feature_string_alt = "ARTHRITIS_CrudePrev"
    places_points = get_PLACES_data_float(test_feature_string_alt)
    points_with_hue = get_hue_from_feature_data(places_points)
    features_object = build_feature_layer_object(points_with_hue)
    return jsonify(features_object)

if __name__ == "__main__":
    app.run(debug=True)