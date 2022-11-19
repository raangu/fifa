import pandas as pd
import streamlit as st

list_teams_wc22 = sorted(["Qatar", "Ecuador", "Senegal", "Netherlands",
"England", "Iran", "United States", "Wales",
"Argentina", "Saudi Arabia", "Mexico", "Poland",
"France", "Australia", "Denmark", "Tunisia",
"Spain", "Costa Rica", "Germany", "Japan",
"Belgium", "Canada", "Morocco", "Croatia",
"Brazil", "Serbia", "Switzerland", "Cameroon",
"Portugal", "Ghana", "Uruguay", "South Korea"])

df = pd.read_csv('wcmatches.csv')

#list_teams = list_unique_values = df['home_team'].unique()

col1, col2 = st.columns(2)

with col1:
    team_a = st.selectbox("Team A", list_teams_wc22)
with col2:
    team_b = st.selectbox("Team B", list_teams_wc22)

if team_a == team_b:
    team_a = 'Germany'
    team_b = 'Belgium'


df_matches_won_team_a = df.query("winning_team == @team_a")
df_matches_lost_team_a = df.query("losing_team == @team_a")

df_matches_won_team_b = df.query("winning_team == @team_b")
df_matches_lost_team_b = df.query("losing_team == @team_b")

#print(df_matches_won_team_a.to_string(index=False))

with col1:
    st.write(team_a)
    st.write("Matches won: "+ str(len(df_matches_won_team_a)))
    st.write("Machtes lost: "+str(len(df_matches_lost_team_a)))

with col2:
    st.write("\r\n"+ team_b)
    st.write("Matches won: "+ str(len(df_matches_won_team_b)))
    st.write("Machtes lost: "+str(len(df_matches_lost_team_b)))

list_all_win_lose_ratios = []
list_all_total_games_played = []

for country in list_teams_wc22:
    df_matches_won = df.query("winning_team == @country")
    df_matches_lost = df.query("losing_team == @country")

    list_all_total_games_played.append(len(df_matches_won) + len(df_matches_lost))
    try:
        list_all_win_lose_ratios.append(len(df_matches_won) / len(df_matches_lost))
    except:
        list_all_win_lose_ratios.append(0)

df_countries_ratios = pd.DataFrame(list(zip(list_teams_wc22, list_all_total_games_played, list_all_win_lose_ratios)),columns =['country', 'games_played', 'ratio']).sort_values('ratio', ascending=False)

df_countries_ratios = df_countries_ratios.reset_index()
df_countries_ratios.drop('index')
print(df_countries_ratios.to_string(index=False))

st.write("List of countries")
st.dataframe(df_countries_ratios)
