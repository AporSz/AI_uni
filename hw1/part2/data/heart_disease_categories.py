# Linguistic variables and fuzzy categories for Heart_disease_cleveland_new.csv
# This file provides logical categories for numerical and categorical attributes
# to be used in a Fuzzy Decision Tree.

fuzzy_categories = {
    # ---------------- NUMERICAL / FUZZY ATTRIBUTES ----------------

    "age": {
        "description": "Age of the patient",
        "linguistic_terms": {
            "Young": "age < 40",
            "Middle_Aged": "40 <= age <= 60",
            "Senior": "age > 60"
        }
    },
    "trestbps": {
        "description": "Resting blood pressure (mm Hg)",
        "linguistic_terms": {
            "Normal": "trestbps < 120",
            "Elevated": "120 <= trestbps < 140",
            "High": "trestbps >= 140"
        }
    },
    "chol": {
        "description": "Serum cholesterol in mg/dl",
        "linguistic_terms": {
            "Normal": "chol < 200",
            "Borderline_High": "200 <= chol < 240",
            "High": "chol >= 240"
        }
    },
    "thalach": {
        "description": "Maximum heart rate achieved",
        "linguistic_terms": {
            "Low": "thalach < 120",
            "Medium": "120 <= thalach <= 160",
            "High": "thalach > 160"
        }
    },
    "oldpeak": {
        "description": "ST depression induced by exercise relative to rest",
        "linguistic_terms": {
            "Low": "oldpeak < 1.0",
            "Risk": "1.0 <= oldpeak <= 2.0",
            "Severe": "oldpeak > 2.0"
        }
    },

    # ---------------- DISCRETE / CRISP ATTRIBUTES ----------------

    "cp": {
        "description": "Chest pain type",
        "mapping": {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic"
        }
    },
    "restecg": {
        "description": "Resting electrocardiographic results",
        "mapping": {
            0: "Normal",
            1: "ST-T wave abnormality",
            2: "Left ventricular hypertrophy"
        }
    },
    "slope": {
        "description": "Slope of the peak exercise ST segment",
        "mapping": {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }
    },
    "ca": {
        "description": "Number of major vessels (0-3) colored by flourosopy",
        "mapping": {
            0: "0 vessels",
            1: "1 vessel",
            2: "2 vessels",
            3: "3 vessels"
        }
    },
    "thal": {
        "description": "Thalassemia",
        "mapping": {
            1: "Normal",
            2: "Fixed defect",
            3: "Reversible defect"
        }
    },
    "sex": {
        "description": "Sex of the patient",
        "mapping": {
            0: "Female",
            1: "Male"
        }
    },
    "fbs": {
        "description": "Fasting blood sugar > 120 mg/dl",
        "mapping": {
            0: "False",
            1: "True"
        }
    },
    "exang": {
        "description": "Exercise induced angina",
        "mapping": {
            0: "No",
            1: "Yes"
        }
    },
    "target": {
        "description": "Heart disease diagnosis",
        "mapping": {
            0: "No Disease",
            1: "Disease Present"
        }
    }
}
