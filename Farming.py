import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

data=pd.read_csv("mean.csv")
final_model = pickle.load(open('model.pkl', 'rb'))
labels=np.load("labels.npy")
crop_mean_data=pd.pivot_table(data,index=['label'],aggfunc='mean')

def meand(x):
    y=crop_mean_data.loc[x]
    return y


st.title("Naturo Intelligent Farming")
st.markdown(
    """
    ### Based on Precision agriculture :- 
    It is budding in India. Precision agriculture is the technology of “site-specific” farming. It has provided us with the advantage of efficient input, output and better decisions regarding farming.
    - Not all precision agriculture systems provide accurate results.
    - In agriculture it is important that the recommendations made are accurate and precise because incase of errors it may lead to heavy material and capital loss.
"""
)
activities=["Crop Prediction","Minimum Nutrition Checker"]
option=st.sidebar.selectbox("Chose your Need",activities)
st.subheader(option)

if option=="Crop Prediction":
    col1, col2  = st.columns(2)
    with col1:
        N=float(st.number_input("Nitrogen (N)"))
        P=float(st.number_input("Phosphorus (P)"))
        K=float(st.number_input("Potassium (K)"))
    with col2 :
        humidity=float(st.number_input("Humidity"))
        ph=float(st.number_input("Ph"))
        rainfall=float(st.number_input("Rainfall (In mm)")) 
    temperature=float(st.number_input("Temperature (In ºC)"))
    btn=st.button("Predict the Crop")
    if btn:
        if N == 0 or P == 0 or K==0 or temperature==0 or ph==0 or rainfall == 0:
            st.text("Processing, please wait .....")
            st.text("WARNING⚠️")
            st.text("Kindly enter correct data (No zero value should be passed)")
        else:
            st.text("Processing, please wait .....")
            pred=(final_model.predict(np.array([[N,P,K,temperature,humidity,ph,rainfall]])))
            x=pred[0]
            st.subheader("You can grow " + str(x) + " in your field")
            st.subheader("The minimum required nutrition for "+ str(x) + " is :")
            st.text(meand(x))

elif option=="Minimum Nutrition Checker":
   
    st.markdown("""
                #### Dear visitor you can check minimum nutrition for 22 types of crops: """)
    col1,col2,col3,col4=st.columns(4)
    x=['Rice', 'Maize', 'Chickpea', 'Kidneybeans', 'Pigeonpeas',
       'Mothbeans', 'Mungbean', 'Blackgram', 'Lentil', 'Pomegranate',
       'Banana', 'Mango', 'Grapes', 'Watermelon', 'Muskmelon', 'Apple',
       'Orange', 'Papaya', 'Coconut', 'Cotton', 'Jute', 'Coffee']
    lbl=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    for i in range(0,6):
        col1.write(x[i])
    for i in range(6,12):
        col2.write(x[i])
    for i in range(12,18):
        col3.write(x[i])
    for i in range(18,22):
        col4.write(x[i])
    z=st.text_input('Enter the crop name (All letters must be small !!):')
    btn2=st.button("Check the Minimum Requirement")
    if btn2:
        if z in lbl:
            st.subheader("The minimum required nutrition for "+ str(z) + " is :")
            st.text((meand(z)))
        else :
            st.text("WARNING⚠️")
            st.text("Kindly enter correct name!! (All letters must be small)")
            
