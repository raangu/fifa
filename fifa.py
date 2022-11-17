import pandas as pd
import streamlit as st
#print("hello")


df = pd.read_csv('wcmatches.csv')

print(df)

st.dataframe(df)