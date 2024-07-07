# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:51:19 2024

@author: ASUS
"""

# Importing the necessary libraries

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np

# Loading the instance of FastAPI into a variable
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
# Loading the saved model
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_parameters.Pregnancies
    glu = input_parameters.Glucose
    bp = input_parameters.BloodPressure
    skin = input_parameters.SkinThickness
    insulin = input_parameters.Insulin
    bmi = input_parameters.BMI
    dpf = input_parameters.DiabetesPedigreeFunction
    age = input_parameters.Age
    
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return "The person is not Diabetic"
    else:
        return "The person is Diabetic"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    