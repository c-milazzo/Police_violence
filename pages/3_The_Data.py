import streamlit as st
import pandas as pd

df1 = pd.read_csv("static/fatal-police-shootings-data.csv")
df2 = pd.read_csv("static/fatal-police-shootings-agencies.csv")

st.title("The Data:")
st.divider()

st.subheader("Fatal Police Shootings:")
st.write(df1)
st.divider()

st.subheader("Agencies of Fatal Police Shootings:")
st.write(df2)


