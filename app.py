import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_option("deprecation.showPyplotGlobalUse", False)
st.title("Retail Store Analysis Dashboard")
st.sidebar.title("Toggle Options")


@st.cache(persist=True)
def load_data():
    data = pd.read_csv("SampleSuperstore.csv")
    return data


data = load_data()
