import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
import matplotlib.pyplot as plt
from pprint import pprint

from pages.Homepage.py import check_password

if check_password():
    st.write("#Page 1 👋")


st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Zona fisica")


'''RPE, Wellness = st.tabs(["RPE", "WELLNESS"])

with RPE:
  

with Wellness:
'''

  



st.caption("Mattia Rampazzo - Vfc u19")
