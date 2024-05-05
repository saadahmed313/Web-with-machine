import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.preprocessing import PowerTransformer

df = pd.read_csv("dataset.csv")

def show_explore_pag():
    num_cols = ["bmi", "avg_glucose_level", "age"]
    cat_cols = list(df.drop(columns=num_cols + ["stroke"]).columns)
    target_col = "stroke"

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    st.write("### Histogram for Stroke Numerical Columns")
    for i, col in enumerate(num_cols):
        sns.histplot(data=df, x=col, ax=ax[i], hue=target_col, kde=True, bins=50)
    st.pyplot(fig)

    st.write("### Countplot for Stroke Output")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="stroke", ax=ax)
    st.pyplot(fig)

    st.write("### Countplot for Smoking Status")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="smoking_status", ax=ax)
    st.pyplot(fig)

    st.write("### Countplot for Work Type")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="work_type", ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45) 
    st.pyplot(fig)