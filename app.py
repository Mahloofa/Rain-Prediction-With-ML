import streamlit as st
import pickle
from PIL import Image


def main():
    st.title(":rainbow[Rain Prediction]")
    image =Image.open('rain.jpg')
    st.image(image,width=800)

    MinTemp = st.text_input(":red[MinTemp]","Type_here")
    MaxTemp = st.text_input(":green[MaxTemp]","Type_here")
    Rainfall = st.text_input(":blue[Rainfall]","Type_here")
    WindGustDir = st.text_input(":red[WindGustDir]","Type_here")
    WindGustSpeed = st.text_input(":green[WindGustSpeed]","Type_here")
    WindDir9am = st.text_input(":blue[WindDir9am]","Type_here")
    WindDir3pm = st.text_input(":red[WindDir3pm]","Type_here")
    WindSpeed9am = st.text_input(":green[WindSpeed9am]","Type_here")
    WindSpeed3pm = st.text_input(":blue[WindSpeed3pm]","Type_here")
    Humidity9am = st.text_input(":red[Humidity9am ]","Type_here")
    Humidity3pm = st.text_input(":green[Humidity3pm]","Type_here")
    Pressure9am = st.text_input(":blue[Pressure9am]","Type_here")
    Pressure3pm = st.text_input(":green[Pressure3pm]","Type_here")
    Temp9am = st.text_input(":blue[Temp9am]","Type_here")
    Temp3pm = st.text_input(":red[Temp3pm]","Type_here")
    RainToday = st.text_input(":green[RainToday]","Type_here")
    
    
    features = [MinTemp,MaxTemp,Rainfall,WindGustDir,WindGustSpeed,WindDir9am, WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm,RainToday]

    model = pickle.load(open('model11.sav','rb'))
    scaler = pickle.load(open('scaler11.sav','rb'))

    pred = st.button('PREDICT')

    if pred:
          prediction=model.predict(scaler.transform([features]))

          if prediction==0:
                st.write(" Raining")

          else:
                st.write(" No Rain")


main()
