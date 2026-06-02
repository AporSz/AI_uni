import numpy as np

class FuzzyUtils:

    def __init__(self):
        self.config = config


    @staticmethod
    def fuzzy_triangle(x, a, b, c):
        rising_edge = (x - a) / (b - a)
        falling_edge = (x - c) / (b - c)

        return np.maximum(0, np.minimum(rising_edge, falling_edge))

    @staticmethod
    def fuzzy_trapezoid(x, a, b, c, d):
        rising_edge = (x - a) / (b - a)
        falling_edge = (d - x) / (d - c)

        return np.maximum(0, np.minimum(np.minimum(rising_edge, 1), falling_edge))

    def attribute_membership(self, attribute, value):
        arr = []
        for _ , func in self.config[attribute].items():
            arr.append(func(value))

        return np.array(arr)

config = {
            "age": {
                "Young": lambda x: FuzzyUtils.fuzzy_trapezoid(x, -1, 0, 35, 50),
                "Middle_Aged": lambda x: FuzzyUtils.fuzzy_triangle(x, 35, 50, 65),
                "Senior": lambda x: FuzzyUtils.fuzzy_trapezoid(x, 50, 65, 120, 121),
            },
            "chol": {
                "Normal": lambda x: FuzzyUtils.fuzzy_trapezoid(x, -1, 0, 180, 220),
                "Borderline_High": lambda x: FuzzyUtils.fuzzy_triangle(x, 180, 220, 260),
                "High": lambda x: FuzzyUtils.fuzzy_trapezoid(x, 220, 260, 600, 601),
            },
            "trestbps": {
                "Normal": lambda x: FuzzyUtils.fuzzy_trapezoid(x, -1, 0, 110, 130),
                "Elevated": lambda x: FuzzyUtils.fuzzy_triangle(x, 110, 130, 150),
                "High": lambda x: FuzzyUtils.fuzzy_trapezoid(x, 130, 150, 300, 301),
            },
            "thalach": {
                "Low": lambda x: FuzzyUtils.fuzzy_trapezoid(x, -1, 0, 100, 140),
                "Medium": lambda x: FuzzyUtils.fuzzy_triangle(x, 100, 140, 160),
                "High": lambda x: FuzzyUtils.fuzzy_trapezoid(x, 140, 160, 300, 301),
            },
            "oldpeak": {
                "Low": lambda x: FuzzyUtils.fuzzy_trapezoid(x, -1, 0, 0.5, 1.5),
                "Risk": lambda x: FuzzyUtils.fuzzy_triangle(x, 0.5, 1.5, 2.5),
                "Severe": lambda x: FuzzyUtils.fuzzy_trapezoid(x, 1.5, 2.5, 10, 11),
            },
            "cp": {
                "Typical Angina": lambda x: int(x == 0),
                "Atypical Angina": lambda x: int(x == 1),
                "Non-anginal Pain": lambda x: int(x == 2),
                "Asymptomatic": lambda x: int(x == 3)
            },
            "restecg": {
                "Normal": lambda x: int(x == 0),
                "ST-T wave abnormality": lambda x: int(x == 1),
                "Left ventricular hypertrophy": lambda x: int(x == 2),
            },
            "slope": {
                "Upsloping": lambda x: int(x == 0),
                "Flat": lambda x: int(x == 1),
                "Downsloping": lambda x: int(x == 2),
            },
            "ca": {
                "0 vessels": lambda x: int(x == 0),
                "1 vessels": lambda x: int(x == 1),
                "2 vessels": lambda x: int(x == 2),
                "3 vessels": lambda x: int(x == 3),
            },
            "thal": {
                "Normal": lambda x: int(x == 0),
                "Fixed defect": lambda x: int(x == 1),
                "Reversible defect": lambda x: int(x == 2),
            },
            "sex": {
                "Female": lambda x: int(x == 0),
                "Male": lambda x: int(x == 1),
            },
            "fbs": {
                "False": lambda x: int(x == 0),
                "True": lambda x: int(x == 1),
            },
            "exang": {
                "No": lambda x: int(x == 0),
                "Yes": lambda x: int(x == 1),
            },
            "target": {
                "No Disease": lambda x: int(x == 0),
                "Disease Present": lambda x: int(x == 1),
            },
        }