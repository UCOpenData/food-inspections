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

    #path = 'Food_Inspections_-_7_1_2018_-_Present_20250430.csv'
    path = os.path.join(DATA_DIR, 'Food_Inspections_-_7_1_2018_-_Present_20250430.csv')

   
    #crash_pd = pd.read_csv(crash_path)
    df = pd.read_csv(path)


    return df

data = load_data()