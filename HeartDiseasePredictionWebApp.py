# -*- coding: utf-8 -*-
"""
Created on Fri Oct  02 19:50:23 2022

@author: Mishal
"""

import numpy as np
import pickle
import streamlit as st
import base64

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


def add_bg_from_local(image_file):
    with open('bg.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )    
    
#creating a function for prediction

def heart_disease(input_data):

    #change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if(prediction[0]==0):
      return "The person does not have Heart Disease."
    else:
      return "The person have Heart Disease."
  

  
def main():
    
    add_bg_from_local('bg.jpg')
    
    #giving a title
    st.title('Heart Disease Prediction Web App')
    
    #getting the input data from the user
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,
    
    age = st.number_input('Age', help='age of patient')
    sex = st.selectbox('Gender', ('Male','Female'),help='gender of patient')
    if sex=='Male': sex=1
    else: sex=0
    cp = st.selectbox('Chest Pain Type', ('Typical Angina','Atypical Angina','Non-anginal pain','Asymptotic'),help='the type of chest-pain experienced by the individual')
    if cp == 'Typical Angina': cp=0
    elif cp == 'Atypical Angina': cp=1
    elif cp == 'Non-anginal pain': cp =2
    else: cp=3
    #cp = st.number_input('Chest Pain Type')
    #st.write('chest-pain experienced by the individual using the following format : 1 = typical angina 2 = atypical angina 3 = non - anginal pain 4 = asymptotic')
    trestbps = st.number_input('Resting Blood Pressure (in mmHg)',help='the resting blood pressure value of an individual in mmHg (unit)')
    chol = st.number_input('Serum Cholestrol (in mg/dl)')
    fbs = st.number_input('Fasting Blood Sugar ', help='compares the fasting blood sugar value of an individual with 120mg/dl. If fasting blood sugar > 120mg/dl then : 1 (true) else : 0 (false)')
    restecg = st.selectbox('Resting ECG', ('Normal','having ST-T wave abnormality','left venticular hyperthropy'))
    if restecg=='Normal': restecg=0
    elif restecg=='having ST-T wave abnormality': restecg=1
    else: restecg=2
    thalach = st.number_input('Max heart rate achieved',help='displays the max heart rate achieved by an individual.')
    exang = st.number_input('Exercise induced angina')
    oldpeak = st.number_input('ST depression')
    slope = st.selectbox('Peak exercise ST segment',('upsloping','flat','downsloping'))
    if slope=='upsloping': slope=0
    elif slope=='flat': slope=1
    else: slope=2
    ca = st.number_input('Number of major vessels (0-3)',help=' colored by flourosopy')
    thal = st.number_input('Thalassemia')
    
    #code for prediction
    
    diagnosis = ''
    
    #creating a button for prediction
    
    if(st.button('Test Result')):
        diagnosis = heart_disease([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()
 
