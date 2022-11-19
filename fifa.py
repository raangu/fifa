import pandas as pd
import streamlit as st
#print("hello")

list_teams_wc22 = ["Qatar", "Ecuador", "Senegal", "Netherlands",
"England", "Iran", "USA", "Wales",
"Argentina", "Saudi Arabia", "Mexico", "Poland",
"France", "Australia", "Denmark", "Tunisia",
"Spain", "Costa Rica", "Germany", "Japan",
"Belgium", "Canada", "Morocco", "Croatia",
"Brazil", "Serbia", "Switzerland", "Cameroon"
"Portugal", "Ghana", "Uruguay", "South Korea"]

df = pd.read_csv('wcmatches.csv')


list_teams = list_unique_values = df['home_team'].unique()

team_a = st.selectbox("Team A", list_teams_wc22)
team_b = st.selectbox("Team B", list_teams)

st.dataframe(df)