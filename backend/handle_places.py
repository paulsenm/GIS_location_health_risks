import csv
from statistics import mean, median, stdev
import matplotlib.pyplot as plt
import numpy as np

def get_places_oregon_test():
    with open('data/PLACES__Census_Tract_Data.csv', 'r') as places_file:
        cancer_prev_stats_array = []
        oregon_points = {
            "type": "FeatureCollection",
            "features": []
        }
        csvreader = csv.DictReader(places_file)
        fields = next(csvreader)
        for row in csvreader:
            if row['StateDesc'] == 'Oregon':
                coords_raw = row['Geolocation']
                coords_cleaned = coords_raw.replace('POINT (', '').replace(')', '')
                coords_array = coords_cleaned.split()
                coords_array[0] = float(coords_array[0])
                coords_array[1] = float(coords_array[1])

                cancer_prevelance = float(row['CANCER_CrudePrev'])
                cancer_prev_stats_array.append(cancer_prevelance)

                severity_group_string = get_severity_color_cancer_OR(cancer_prevelance)

                feature_to_add = {
                    "type": "Feature",
                    "properties": {"name": f"cancer prev: {str(cancer_prevelance)}", "severity_group": severity_group_string},
                    "geometry": {
                        "type": "Point",
                        "coordinates": coords_array
                    }
                }
                
                oregon_points['features'].append(feature_to_add)
        #print(oregon_points)
        # plt.hist(cancer_prev_stats_array, bins=18)
        # plt.show()
        print(f'mean: {mean(cancer_prev_stats_array)}, median: {median(cancer_prev_stats_array)}, std dev: {stdev(cancer_prev_stats_array)}')
    return oregon_points

def get_severity_color_cancer_OR(prevelance:float):
    LOW_STRING = 'low'
    MEDIUM_STRING = 'medium'
    HIGH_STRING = 'high'
    VERY_HIGH_STRING = 'very-high'
    GREEN_MAX = 5
    YELLOW_MAX = 9
    RED_MAX = 12
    if prevelance < GREEN_MAX:
        print("low value returned")
        return LOW_STRING
    if prevelance < YELLOW_MAX:
        return MEDIUM_STRING
    if prevelance < RED_MAX:
        return HIGH_STRING
    return VERY_HIGH_STRING