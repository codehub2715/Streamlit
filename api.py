#'http://api.weatherapi.com/v1/current.json?key=2bc06959bf9642e1a52171957251702&q='

import streamlit as st
import requests

st.title("Weather APP")

city = st.text_input("Enter City Name")

if city:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a4bb0a0f9159b8beb76e423feb3bb385'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        st.write('Temperature:', data['main']['temp'])
        st.write('Weather:', data['weather'][0]['description'])
    else:
        st.write('City not found')
