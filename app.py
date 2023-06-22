import pickle
import streamlit as st

df = pickle.load(open('heart_disease_model.sav', 'rb'))

st.title('Heart Disease Prediction using ML')
age = st.text_input('Age')
sex = st.text_input('Sex')
cp = st.text_input('Chest Pain types')
trestbps = st.text_input('Resting Blood Pressure')
chol = st.text_input('Serum Cholestoral in mg/dl')
fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
restecg = st.text_input('Resting Electrocardiographic results')
thalach = st.text_input('Maximum Heart Rate achieved')
exang = st.text_input('Exercise Induced Angina')
oldpeak = st.text_input('ST depression induced by exercise')
slope = st.text_input('Slope of the peak exercise ST segment')
ca = st.text_input('Major vessels colored by flourosopy')
thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

heart_diagnosis = ''

if st.button('Heart Disease Test Result'):
    
    age = int(age)
    sex = int(sex)
    cp = int(cp)
    chol = int(chol)
    trestbps = int(trestbps)
    restecg = int(restecg)
    fbs = int(fbs)
    thalach = int(thalach)
    exang = int(exang)
    oldpeak = float(oldpeak)
    slope = int(slope)
    ca = int(ca)
    thal = int(thal)

    heart_prediction = df.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                              
        
    if (heart_prediction[0] == 1):
      heart_diagnosis = 'The person is having heart disease'
    else:
       heart_diagnosis = 'The person does not have any heart disease'
        
st.success(heart_diagnosis)
        