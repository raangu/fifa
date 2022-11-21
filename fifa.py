import pandas as pd
import streamlit as st

st.subheader("Statistics for the last 5 World Cups")

list_teams_wc22 = sorted(["Qatar", "Ecuador", "Senegal", "Netherlands",
"England", "Iran", "United States", "Wales",
"Argentina", "Saudi Arabia", "Mexico", "Poland",
"France", "Australia", "Denmark", "Tunisia",
"Spain", "Costa Rica", "Germany", "Japan",
"Belgium", "Canada", "Morocco", "Croatia",
"Brazil", "Serbia", "Switzerland", "Cameroon",
"Portugal", "Ghana", "Uruguay", "South Korea"])

df = pd.read_csv('wcmatches.csv', index_col=False)

#list_teams = list_unique_values = df['home_team'].unique()

col1, col2 = st.columns(2)

with col1:
    team_a = st.selectbox("Team A", list_teams_wc22)
with col2:
    team_b = st.selectbox("Team B", list_teams_wc22)


# all time matches
df_matches_won_team_a = df.query("winning_team == @team_a")
df_matches_lost_team_a = df.query("losing_team == @team_a")

df_matches_won_team_b = df.query("winning_team == @team_b")
df_matches_lost_team_b = df.query("losing_team == @team_b")

#with col1:
#    st.write("All Time")
#    st.write("Won: "+ str(len(df_matches_won_team_a)))
#    st.write("Lost: "+str(len(df_matches_lost_team_a)))

#with col2:
#    st.write("All Time")
#    st.write("Won: " + str(len(df_matches_won_team_b)))
#    st.write("Lost: "+str(len(df_matches_lost_team_b)))


# recent matches
df_recent_matches_won_team_a = df.query("winning_team == @team_a and year>2000")
df_recent_matches_lost_team_a = df.query("losing_team == @team_a and year>2000")

df_recent_matches_won_team_b = df.query("winning_team == @team_b and year>2000")
df_recent_matches_lost_team_b = df.query("losing_team == @team_b and year>2000")

with col1:
    #st.write("Last 5 World Cups")
    st.write("Won: "+ str(len(df_recent_matches_won_team_a)))
    st.write("Lost: "+str(len(df_recent_matches_lost_team_a)))

with col2:
    #st.write("Last 5 World Cups")
    #st.write("\r\n"+ team_b)
    st.write("Won: " + str(len(df_recent_matches_won_team_b)))
    st.write("Lost: "+str(len(df_recent_matches_lost_team_b)))

list_all_win_lose_ratios = []
list_all_wins = []
list_all_losses = []
list_all_total_games_played = []
list_all_total_goals_won = []
#list_all_total_goals_lost = []

for country in list_teams_wc22:
    df_matches_won = df.query("winning_team == @country and year>2000")
    df_matches_lost = df.query("losing_team == @country and year>2000")

    df_matches_won_home = df_matches_won.query("home_team == @country")
    df_matches_won_away = df_matches_won.query("away_team == @country")

    total_goals_won = df_matches_won_home['home_score'].sum()
    total_goals_won = total_goals_won + df_matches_won_away['away_score'].sum()

    try:
        list_all_total_goals_won.append(total_goals_won / len(df_matches_won))
    except:
        list_all_total_goals_won.append(0)

    #df_matches_lost_home = df_matches_lost.query("home_team == @country")
    #df_matches_lost_away = df_matches_lost.query("away_team == @country")

    #total_goals_lost = df_matches_lost_home.sum('home_score')
    #total_goals_lost = total_goals_lost + df_matches_lost_away.sum('away_score')

    list_all_total_games_played.append(len(df_matches_won) + len(df_matches_lost))
    list_all_wins.append(len(df_matches_won))
    list_all_losses.append(len(df_matches_lost))
    try:
        list_all_win_lose_ratios.append(len(df_matches_won) / len(df_matches_lost))
    except:
        list_all_win_lose_ratios.append(0)

df_countries_ratios = pd.DataFrame(list(zip(list_teams_wc22, list_all_total_games_played, list_all_wins, list_all_losses, list_all_total_goals_won, list_all_win_lose_ratios)),columns =['Country', 'Total Matches', 'Won', 'Lost', 'Avg. Winning Goals', 'W/L ratio']).sort_values('W/L ratio', ascending=False)

df_countries_ratios.set_index('Country', inplace=True)

#st.write("List of countries")
st.table(df_countries_ratios)
