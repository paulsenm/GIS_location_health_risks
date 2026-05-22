import csv



with open('data/PLACES__Census_Tract_Data.csv', 'r') as places_file:
    oregon_points = {
        "type": "FeatureCollection",
        "features": []
    }
    csvreader = csv.DictReader(places_file)
    fields = next(csvreader)
    for row in csvreader:
        if row['StateDesc'] == 'Oregon':
            coords = row['Geolocation']
            oregon_points['features'].append(coords)
    print(oregon_points)
