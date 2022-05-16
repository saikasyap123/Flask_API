import pickle
import json
import numpy as np

__data_columns = None
__locations = None
__model = None

def get_locations():
    load_artifacts()
    return __locations


def load_artifacts():
    global __locations
    global __data_columns
    global __model
    with open("../model/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('../model/Banglore_house_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)

def predict_price(bhk, bathrooms, balcony, area):
    load_artifacts()
    global __data_columns
    temp = np.zeros(len(__data_columns))
    temp[0] = bhk
    temp[1] = bathrooms
    temp[2] = balcony
    try:
        loc_index = np.where(__data_columns==area)[0][0]
    except:
        loc_index = -1
    if loc_index>=0:
        temp[loc_index] = 1
    price = round(__model.predict([temp])[0], 2)
    return price
if __name__=="__main__":
    load_artifacts()
    #print(get_locations())
    print(predict_price(2, 2, 1, 245))