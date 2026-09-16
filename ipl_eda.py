"""
IPL Data Analysis — Exploratory Data Analysis (EDA) Project
Author: Prince Kumar

Dataset: "IPL Complete Dataset (2008-2020)" by patrickb1912 on Kaggle
Files needed: matches.csv, deliveries.csv
Download from: https://www.kaggle.com/datasets/patrickb1912/ipl-complete-csv-20082020

HOW TO USE:
1. Download matches.csv and deliveries.csv from the Kaggle link above.
2. Place them in the same folder as this script.
3. Run: python ipl_eda.py  (or paste sections into Jupyter/Colab cells)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# STEP 1: Load the data
# ---------------------------------------------------------
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("Matches shape:", matches.shape)
print("Deliveries shape:", deliveries.shape)
print(matches.head())

# ---------------------------------------------------------
# STEP 2: Clean the data
# ---------------------------------------------------------
# Check missing values
print("\nMissing values in matches.csv:\n", matches.isnull().sum())

# Fill missing 'city' using venue info, drop rows with no result
matches['city'] = matches['city'].fillna('Unknown')
matches = matches.dropna(subset=['winner'])

# Standardize team names (some datasets have renamed franchises)
matches.replace(
    {'Delhi Daredevils': 'Delhi Capitals',
     'Deccan Chargers': 'Sunrisers Hyderabad'},
    inplace=True
)

# ---------------------------------------------------------
# STEP 3: Basic Exploration
# ---------------------------------------------------------
# Total matches played each season
matches_per_season = matches['season'].value_counts().sort_index()
print("\nMatches per season:\n", matches_per_season)

# Team with most wins overall
top_teams = matches['winner'].value_counts().head(10)
print("\nTop winning teams:\n", top_teams)

# Toss decision trends (bat vs field)
toss_decision = matches['toss_decision'].value_counts()
print("\nToss decisions:\n", toss_decision)

# Does winning the toss help win the match?
toss_match_same = (matches['toss_winner'] == matches['winner']).mean() * 100
print(f"\nToss winner also won the match: {toss_match_same:.2f}% of the time")

# ---------------------------------------------------------
# STEP 4: Visualizations
# ---------------------------------------------------------

# Chart 1 — Matches played per season
plt.figure(figsize=(10, 5))
matches_per_season.plot(kind='bar', color='steelblue')
plt.title("Matches Played Per IPL Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.savefig("chart1_matches_per_season.png")
plt.close()

# Chart 2 — Top 10 winning teams
plt.figure(figsize=(10, 5))
top_teams.plot(kind='barh', color='seagreen')
plt.title("Top 10 Teams by Total Wins")
plt.xlabel("Wins")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("chart2_top_teams.png")
plt.close()

# Chart 3 — Toss decision trend over seasons
toss_by_season = matches.groupby(['season', 'toss_decision']).size().unstack()
toss_by_season.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.title("Toss Decision Trend by Season (Bat vs Field)")
plt.xlabel("Season")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart3_toss_trend.png")
plt.close()

# ---------------------------------------------------------
# STEP 5: Player-level analysis (using deliveries.csv)
# ---------------------------------------------------------
# Top run scorers
top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 run scorers:\n", top_batsmen)

plt.figure(figsize=(10, 5))
top_batsmen.plot(kind='barh', color='darkorange')
plt.title("Top 10 Run Scorers (All Seasons)")
plt.xlabel("Total Runs")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("chart4_top_batsmen.png")
plt.close()

# Top wicket takers (dismissal_kind not null means a wicket fell)
wickets = deliveries[deliveries['dismissal_kind'].notnull()]
top_bowlers = wickets['bowler'].value_counts().head(10)
print("\nTop 10 wicket takers:\n", top_bowlers)

plt.figure(figsize=(10, 5))
top_bowlers.plot(kind='barh', color='firebrick')
plt.title("Top 10 Wicket Takers (All Seasons)")
plt.xlabel("Wickets")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("chart5_top_bowlers.png")
plt.close()

print("\nAll charts saved as PNG files. Analysis complete!")
