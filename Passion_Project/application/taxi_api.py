import numpy as np
import pickle

ETA_predictor = pickle.load(open('ETA_predictor.pkl', 'rb'))
fare_predictor = pickle.load(open('fare_predictor.pkl', 'rb'))

test_ride = {}

def make_prediction(features):
    feat_space = np.array([features['age'], int(features['address'] == 'U'), features['Medu'], features['Fedu'], features['studytime'],
                           features['failures'], features['paid'], features['higher'], features['famrel'], features['freetime'],
                           features['goout'], features["Walc"], features['health'], features['absences'],
                           int(features['discipline'] == 'maths')]).reshape(1,-1)

    ETA = ETA_predictor.get_ETA(feat_space)
    fare = fare_predictor.get_fare(feat_space)


    result = {
        'ETA': ,
        'fare':
    }
    return result


if __name__ == '__main__':
    print(make_prediction(test_ride))
