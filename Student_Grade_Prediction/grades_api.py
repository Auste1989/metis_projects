import numpy as np
import pickle

Random_Forest = pickle.load(open('Student_Grade_Predictor.pkl', 'rb'))

test_student = {'age': 15, 'address': 'U', 'Medu': 4, 'Fedu': 4,
                'studytime': 5, 'failures': 1, 'paid': 0, 'higher': 1,
                'famrel': 4, 'freetime': 5, 'goout': 1, 'Walc': 1,
                'health': 5, 'absences': 10, 'discipline': 'maths'}

def make_prediction(features):
    feat_space = np.array([features['age'], int(features['address'] == 'U'), features['Medu'], features['Fedu'], features['studytime'],
                           features['failures'], features['paid'], features['higher'], features['famrel'], features['freetime'],
                           features['goout'], features["Walc"], features['health'], features['absences'],
                           int(features['discipline'] == 'maths')]).reshape(1,-1)

    prob_pass = round(Random_Forest.predict_proba(feat_space)[0, 1] * 100, 0)

    result = {
        'prediction': int(prob_pass > 50),
        'prob_pass': prob_pass
    }
    return result


if __name__ == '__main__':
    print(make_prediction(test_student))
