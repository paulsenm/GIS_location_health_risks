import csv
from statistics import mean, median, stdev
import matplotlib.pyplot as plt
import numpy as np

PREV_MIN = 0
PREV_MAX = 100

def get_PLACES_data_float(layer_name):
    feature_values_array = []
    with open('data/PLACES__Census_Tract_Data.csv', 'r') as places_file:
        csvreader = csv.DictReader(places_file)
        for row in csvreader:
            feature_coords_item = {}
            coords_raw = row['Geolocation']
            coords_cleaned = coords_raw.replace('POINT (', '').replace(')', '')
            coords_array = coords_cleaned.split()
            coords_array[0] = float(coords_array[0])
            coords_array[1] = float(coords_array[1])
            if row[layer_name] != '':
                feature_value = float(row[layer_name])
            else:
                feature_value = -1
            print(f'getting value for {layer_name}. value was {feature_value}')

            feature_coords_item['coords_array'] = coords_array
            feature_coords_item['feature_value'] = feature_value

            feature_values_array.append(feature_coords_item)
        
    return feature_values_array

def map_severity_to_hue(severity, severity_min, severity_max, hue_min, hue_max):
    severity_range = severity_max - severity_min
    hue_range = hue_max - hue_min

    hue_value = ((severity - severity_min) / severity_range) * hue_range + hue_min

    return hue_value

def get_hue_from_feature_data(feature_data):
    feature_data_with_hue = []
    values = [feature['feature_value'] for feature in feature_data]
    minimum_feature_value = np.min(values)
    maximum_feature_value = np.max(values)
    
    for feature in feature_data:
        new_feature_data_with_hue_item = {}
        hue = map_severity_to_hue(feature['feature_value'], minimum_feature_value, maximum_feature_value, PREV_MIN, PREV_MAX)
        new_feature_data_with_hue_item['hue'] = int(hue)
        new_feature_data_with_hue_item['feature_value'] = feature['feature_value']
        new_feature_data_with_hue_item['coords_array'] = feature['coords_array']
        print(f'hue was: {new_feature_data_with_hue_item['hue']}')
        
        feature_data_with_hue.append(new_feature_data_with_hue_item)
    
    return feature_data_with_hue


def build_feature_layer_object(location_hue_data):
    feature_layer_structure = {
        "type": "FeatureCollection",
        "features": []
    }
    for feature_point in location_hue_data:
        prevalence = feature_point['feature_value']
        coords_array = feature_point['coords_array']
        hue = feature_point['hue']
        feature_to_add = {
                "type": "Feature",
                "properties": {
                    "name": f"Prevalence: {str(prevalence)}",
                    "hue": hue
                    },
                "geometry": {
                    "type": "Point",
                    "coordinates": coords_array
                }
            }
        
        feature_layer_structure['features'].append(feature_to_add)
    print(f'total number of features: {str(len(feature_layer_structure))}')
    print(f'feature object: {feature_layer_structure}')
    return feature_layer_structure

def get_severity_color_cancer_OR(prevalence:float):
    LOW_STRING = 'low'
    MEDIUM_STRING = 'medium'
    HIGH_STRING = 'high'
    VERY_HIGH_STRING = 'very-high'
    GREEN_MAX = 8
    YELLOW_MAX = 11
    RED_MAX = 14
    if prevalence < GREEN_MAX:
        print("low value returned")
        return LOW_STRING
    if prevalence < YELLOW_MAX:
        return MEDIUM_STRING
    if prevalence < RED_MAX:
        return HIGH_STRING
    return VERY_HIGH_STRING