from flask import Flask, jsonify
from flask_cors import CORS

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

if __name__ == "__main__":
    app.run(debug=True)