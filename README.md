# IPL Match & Player Performance Analysis

An Exploratory Data Analysis (EDA) project on IPL (Indian Premier League) cricket data, built using Python.

## 📌 Objective
To analyze IPL match and ball-by-ball data to uncover trends in team performance, toss decisions, and player statistics using data cleaning, aggregation, and visualization.

## 🗂️ Dataset
Based on the structure of the **"IPL Complete Dataset (2008–2020)"** (publicly available on Kaggle), containing:
- `matches.csv` — match-level data (teams, toss, venue, winner, season)
- `deliveries.csv` — ball-by-ball data (runs, wickets, batter, bowler)

> Dataset source: [Kaggle - IPL Complete Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-csv-20082020)

## 🛠️ Tools & Libraries
- **Python**
- **Pandas** — data cleaning and aggregation
- **NumPy** — numerical operations
- **Matplotlib** — data visualization

## 🔍 Analysis Performed
1. **Data Cleaning** — handled missing values, standardized team names across seasons (e.g., renamed franchises)
2. **Season-wise Trends** — matches played per season across 13 seasons (2008–2020)
3. **Team Performance** — top 10 teams by total wins
4. **Toss Analysis** — toss decision trends (bat vs. field) and their relationship with match outcomes
5. **Player Statistics** — top 10 run scorers and top 10 wicket takers across all seasons

## 📊 Key Findings
- Analyzed 750+ matches across 13 IPL seasons
- Teams increasingly chose to field first after winning the toss, reflecting common T20 chasing strategy
- Winning the toss correlated with winning the match only ~52% of the time — showing limited overall impact
- Identified consistent top performers across seasons in both batting and bowling

## 📈 Sample Outputs
See the `charts/` folder for all visualizations:
- Matches played per season
- Top 10 winning teams
- Toss decision trend by season
- Top 10 run scorers
- Top 10 wicket takers

## 🚀 How to Run
1. Download `matches.csv` and `deliveries.csv` from the Kaggle link above
2. Place them in the same folder as `ipl_eda.py`
3. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib
   ```
4. Run the script:
   ```bash
   python ipl_eda.py
   ```
5. Charts will be saved as PNG files in the same folder

## 👤 Author
**Prince Kumar**
B.Sc. (Hons.) Statistics, Kirori Mal College, University of Delhi
📧 prince1oct2006@gmail.com
