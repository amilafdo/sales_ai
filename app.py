# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI 
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#defining the classes
class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    
#loading the saved model
diabetes_prediction_model = pickle.load(open('diabetes_model.sav','rb'))

#creating the API

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    pregnancies = input_dictionary['Pregnancies']
    glucose = input_dictionary['Glucose']
    blood_pressure = input_dictionary['BloodPressure']
    skin_thickness = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    diabetes_pedigree_function = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
# passing the data into the model

    input_list = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
    
    prediction = diabetes_prediction_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The Person is not Diabetic'
    else:
        return 'The Person is Diabetic'


