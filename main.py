import pandas as pd
import os
import zipfile
#import folium
import streamlit as st
#from streamlit_folium import folium_static
#import matplotlib.pyplot as plt
#import seaborn as sns
from kaggle.api.kaggle_api_extended import KaggleApi
st.set_page_config(
    page_title="Chicago Food Inspection data",
    layout="wide",
    initial_sidebar_state="expanded",
)
if 'kaggle' in st.secrets:
    os.environ['KAGGLE_USERNAME'] = st.secrets["kaggle"]["username"]
    os.environ['KAGGLE_KEY'] = st.secrets["kaggle"]["key"]
else:
    st.error("Kaggle credentials not found. Please set them in Streamlit secrets.")
    st.stop()
@st.cache_data
def load_data():
    api = KaggleApi()
    api.authenticate()
    dataset_identifier = "catherinetodd123/chicago-restaurant-inspections"  
    DATA_DIR = 'data'
    os.makedirs(DATA_DIR, exist_ok=True)

    
    api.dataset_download_files(dataset_identifier, path=DATA_DIR, unzip=True)

    
    path = os.path.join(DATA_DIR, 'Food_Inspections_-_7_1_2018_-_Present_20250430.csv')

   
    
    df = pd.read_csv(path)


    return df

data = load_data()
zipcodes = sorted(data['Zip'].dropna().unique())
selected_zips = st.sidebar.multiselect("Select ", options=zipcodes, default=[60615, 60637]  )
failed = data[(data['Results'] == 'Fail') & ((data["Zip"].isin(selected_zips)))]
rates = (data.groupby('Results').size().to_frame('Percentage') / data.shape[0] ) * 100
st.write("hello")
st.write(rates)
search_query = st.text_input("Enter a business  name:", None)
st.write(failed)


