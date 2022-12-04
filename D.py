import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as plt

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


st.title("TEMA 4: Visualización de Mapas")
st.subheader("José Luis Quevedo Orrantia")
st.write('Desarrollo de un código sobre la estructura de una aplicación web')


data = load_data(1000)

hour_to_filter = st.slider('hour', 0, 23, 12)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.map(filtered_data)

