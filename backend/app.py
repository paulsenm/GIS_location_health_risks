from flask import Flask, jsonify
from flask_cors import CORS

from handle_places import get_places_oregon_test

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

if __name__ == "__main__":
    app.run(debug=True)