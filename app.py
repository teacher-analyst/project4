# Import flask
from flask import Flask, jsonify
import pandas as pd
import json 
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import pickle

#load in scaler and model
with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)

treem = pickle.load(open('tree_model.sav', 'rb'))

empty_case = pd.DataFrame([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                               0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], 
                               columns=['DAY_OF_WEEK_1', 'DAY_OF_WEEK_2', 'DAY_OF_WEEK_3', 'DAY_OF_WEEK_4', 'DAY_OF_WEEK_5',
                                 'DAY_OF_WEEK_6', 'DAY_OF_WEEK_7', 'ACCIDENT_TYPE_Collision with a fixed object',
                                 'ACCIDENT_TYPE_Collision with vehicle', 'ACCIDENT_TYPE_Fall from or in moving vehicle',
                                 'ACCIDENT_TYPE_No collision and no object struck', 'ACCIDENT_TYPE_Other accident',
                                 'ACCIDENT_TYPE_Struck Pedestrian', 'ACCIDENT_TYPE_Struck animal',
                                 'ACCIDENT_TYPE_Vehicle overturned (no collision)',
                                 'ACCIDENT_TYPE_collision with some other object', 'LIGHT_CONDITION_Dark No street lights',
                                 'LIGHT_CONDITION_Dark Street lights off', 'LIGHT_CONDITION_Dark Street lights on',
                                 'LIGHT_CONDITION_Dark Street lights unknown', 'LIGHT_CONDITION_Day',
                                 'LIGHT_CONDITION_Dusk/Dawn', 'LIGHT_CONDITION_Unk.', 'ROAD_GEOMETRY_Cross intersection',
                                 'ROAD_GEOMETRY_Dead end', 'ROAD_GEOMETRY_Multiple intersection',
                                 'ROAD_GEOMETRY_Not at intersection', 'ROAD_GEOMETRY_Private property',
                                 'ROAD_GEOMETRY_Road closure', 'ROAD_GEOMETRY_T intersection', 'ROAD_GEOMETRY_Unknown',
                                 'ROAD_GEOMETRY_Y intersection','SPEED_ZONE_100 km/hr', 'SPEED_ZONE_110 km/hr',
                                 'SPEED_ZONE_40 km/hr', 'SPEED_ZONE_50 km/hr', 'SPEED_ZONE_60 km/hr', 'SPEED_ZONE_70 km/hr',
                                 'SPEED_ZONE_80 km/hr', 'SPEED_ZONE_90 km/hr', 'SPEED_ZONE_Camping grounds or off road',
                                 'SPEED_ZONE_Not known', 'SPEED_ZONE_Other speed limit', 'RMA_ALL_Arterial Highway',
                                 'RMA_ALL_Arterial Highway,Arterial Other', 'RMA_ALL_Arterial Highway,Local Road',
                                 'RMA_ALL_Arterial Other', 'RMA_ALL_Arterial Other,Arterial Highway',
                                 'RMA_ALL_Arterial Other,Local Road', 'RMA_ALL_Freeway', 'RMA_ALL_Freeway,Arterial Other',
                                 'RMA_ALL_Local Road', 'RMA_ALL_Local Road,Arterial Highway',
                                 'RMA_ALL_Local Road,Arterial Other', 'RMA_ALL_Other', 'SEVERITY_Fatal accident',
                                 'SEVERITY_Non injury accident', 'SEVERITY_Other injury accident',
                                 'SEVERITY_Serious injury accident', 'REGION_NAME_EASTERN REGION',
                                 'REGION_NAME_METROPOLITAN NORTH WEST REGION', 'REGION_NAME_METROPOLITAN SOUTH EAST REGION',
                                 'REGION_NAME_NORTH EASTERN REGION', 'REGION_NAME_NORTHERN REGION', 
                                 'REGION_NAME_SOUTH WESTERN REGION', 'REGION_NAME_WESTERN REGION'])

with open("output.json") as file:
    output_dict  = json.load(file)


def create_case(day_of_week, accident_type, light_condition, road_geometry, speed_zone, road_type, severity, region_name, empty_case):

    case = empty_case

    if day_of_week == 1:
        case['DAY_OF_WEEK_1'] = 1
    elif day_of_week == 2:
        case['DAY_OF_WEEK_2'] = 1
    elif day_of_week == 3:
        case['DAY_OF_WEEK_3'] = 1
    elif day_of_week == 4:
        case['DAY_OF_WEEK_4'] = 1
    elif day_of_week == 5:
        case['DAY_OF_WEEK_5'] = 1
    elif day_of_week == 6:
        case['DAY_OF_WEEK_6'] = 1
    elif day_of_week == 7:
        case['DAY_OF_WEEK_7'] = 1

    if accident_type == 0:
        case['ACCIDENT_TYPE_Collision with a fixed object'] = 1
    elif accident_type == 1:
        case['ACCIDENT_TYPE_Collision with vehicle'] = 1
    elif accident_type == 2:
        case['ACCIDENT_TYPE_Fall from or in moving vehicle'] = 1
    elif accident_type == 3:
        case['ACCIDENT_TYPE_No collision and no object struck'] = 1
    elif accident_type == 4:
        case['ACCIDENT_TYPE_Other accident'] = 1
    elif accident_type == 5:
        case['ACCIDENT_TYPE_Struck Pedestrian'] = 1
    elif accident_type == 6:
        case['ACCIDENT_TYPE_Struck animal'] = 1
    elif accident_type == 7:
        case['ACCIDENT_TYPE_Vehicle overturned (no collision)'] = 1
    elif accident_type == 8:
        case['ACCIDENT_TYPE_collision with some other object'] = 1

    if light_condition == 0:
        case['LIGHT_CONDITION_Dark No street lights'] = 1
    elif light_condition == 1:
        case['LIGHT_CONDITION_Dark Street lights off'] = 1
    elif light_condition == 2:
        case['LIGHT_CONDITION_Dark Street lights on'] = 1
    elif light_condition == 3:
        case['LIGHT_CONDITION_Dark Street lights unknown'] = 1
    elif light_condition == 4:
        case['LIGHT_CONDITION_Day'] = 1
    elif light_condition == 5:
        case['LIGHT_CONDITION_Dusk/Dawn'] = 1
    elif light_condition == 6:
        case['LIGHT_CONDITION_Unk.'] = 1

    if road_geometry == 0:
        case['ROAD_GEOMETRY_Cross intersection'] = 1
    elif road_geometry == 1:
        case['ROAD_GEOMETRY_Dead end'] = 1
    elif road_geometry == 2:
        case['ROAD_GEOMETRY_Multiple intersection'] = 1
    elif road_geometry == 3:
        case['ROAD_GEOMETRY_Not at intersection'] = 1
    elif road_geometry == 4:
        case['ROAD_GEOMETRY_Private property'] = 1
    elif road_geometry == 5:
        case['ROAD_GEOMETRY_Road closure'] = 1
    elif road_geometry == 6:
        case['ROAD_GEOMETRY_T intersection'] = 1
    elif road_geometry == 7:
        case['ROAD_GEOMETRY_Y intersection'] = 1
    elif road_geometry == 8:
        case['ROAD_GEOMETRY_Unknown'] = 1

    if speed_zone == 0:
        case['SPEED_ZONE_100 km/hr'] = 1
    elif speed_zone == 1:
        case['SPEED_ZONE_110 km/hr'] = 1
    elif speed_zone == 2:
        case['SPEED_ZONE_40 km/hr'] = 1
    elif speed_zone == 3:
        case['SPEED_ZONE_50 km/hr'] = 1
    elif speed_zone == 4:
        case['SPEED_ZONE_60 km/hr'] = 1
    elif speed_zone == 5:
        case['SPEED_ZONE_70 km/hr'] = 1
    elif speed_zone == 6:
        case['SPEED_ZONE_80 km/hr'] = 1
    elif speed_zone == 7:
        case['SPEED_ZONE_90 km/hr'] = 1

    if road_type == 0:
        case['RMA_ALL_Arterial Highway'] = 1
    elif road_type == 1:
        case['RMA_ALL_Arterial Highway,Arterial Other'] = 1
    elif road_type == 2:
        case['RMA_ALL_Arterial Highway,Local Road'] = 1
    elif road_type == 3:
        case['RMA_ALL_Arterial Other'] = 1
    elif road_type == 4:
        case['RMA_ALL_Arterial Other,Arterial Highway'] = 1
    elif road_type == 5:
        case['RMA_ALL_Arterial Other,Local Road'] = 1
    elif road_type == 6:
        case['RMA_ALL_Freeway'] = 1
    elif road_type == 7:
        case['RMA_ALL_Freeway,Arterial Other'] = 1
    elif road_type == 8:
        case['RMA_ALL_Local Road'] = 1
    elif road_type == 9:
        case['RMA_ALL_Local Road,Arterial Highway'] = 1
    elif road_type == 10:
        case['RMA_ALL_Local Road,Arterial Highway'] = 1
    elif road_type == 11:
        case['RMA_ALL_Other'] = 1

    if severity == 0:
        case['SEVERITY_Fatal accident'] = 1
    elif severity == 1:
        case['SEVERITY_Other injury accident'] = 1
    elif severity == 2:
        case['SEVERITY_Serious injury accident'] = 1
    
    if region_name == 0:
        case['REGION_NAME_EASTERN REGION'] = 1
    elif region_name == 1:
        case['REGION_NAME_METROPOLITAN NORTH WEST REGION'] = 1
    elif region_name == 2:
        case['REGION_NAME_METROPOLITAN SOUTH EAST REGION'] = 1
    elif region_name == 3:
        case['REGION_NAME_NORTH EASTERN REGION'] = 1
    elif region_name == 4:
        case['REGION_NAME_NORTHERN REGION'] = 1
    elif region_name == 5:
        case['REGION_NAME_SOUTH WESTERN REGION'] = 1
    elif region_name == 6:
        case['REGION_NAME_WESTERN REGION'] = 1
    
    return case 

def load_output(prediction):
    return output_dict[prediction]

# Create the app
app = Flask(__name__)

@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/DAY_OF_WEEK/ACCIDENT_TYPE/LIGHT_CONDITION/ROAD_GEOMETRY/SPEED_ZONE/ROAD_TYPE/SEVERITY/REGION_NAME"
    )

@app.route("/api/v1.0/<day_of_week>/<accident_type>/<light_condition>/<road_geometry>/<speed_zone>/<road_type>/<severity>/<region_name>")
def predict_case(day_of_week, accident_type, light_condition, road_geometry, speed_zone, road_type, severity, region_name):

    case = create_case(day_of_week, accident_type, light_condition, road_geometry, speed_zone, road_type, severity, region_name, empty_case)

    case_scaled = scaler.transform(case)

    prediction = treem.predict(case_scaled)

    response = jsonify(load_output(prediction[0]))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#run in debugging mode
if __name__ == '__main__':
    app.run(debug=True) 