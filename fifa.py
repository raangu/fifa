import pandas as pd
import streamlit as st
#print("hello")


df = pd.read_csv('wcmatches.csv')


list_teams = list_unique_values = df['home_team'].unique()

team_a = st.selectbox("Team A", list_teams)
team_b = st.selectbox("Team B", list_teams)

st.dataframe(df)