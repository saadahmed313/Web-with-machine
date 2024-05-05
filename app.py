import streamlit as st

from predict import show_predict_pag
from explore import show_explore_pag
pag=st.sidebar.selectbox("Explore Or Prediction", ("Predict", "Explore"))
if pag == "Predict":

   show_predict_pag()
else:

    show_explore_pag()