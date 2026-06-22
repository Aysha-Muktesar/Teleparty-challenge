import sqlite3
import pandas as pd


# Connect to SQLite database
conn = sqlite3.connect("teleparty.db")
cursor = conn.cursor()


# Execute schema.sql
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

print("Tables created successfully")


# Read CSV files
shows = pd.read_csv("data/all-series-ep-average.csv")
shows['Rating Count'] = (
    shows['Rating Count']
    .astype(str)
    .str.replace(',', '')
    .astype(int)
)
shows['Rank'] = (
    shows['Rank']
    .astype(str)
    .str.replace(',', '')
    .astype(int)
)

seasons = pd.read_csv("data/top-seasons-full.csv")
episodes = pd.read_csv("data/all-episode-ratings.csv")
#print(episodes["id_code"].duplicated().sum())
#print(episodes.head())
#print("Duplicate id_code:", episodes["id_code"].duplicated().sum())

'''print("Duplicate episodes:",
      episodes.duplicated(
          subset=["Code", "Season", "Episode"]
      ).sum())
      '''


# Rename columns to match schema
shows.columns = [
    "code",
    "title",
    "rating",
    "rating_count",
    "rank",
    "rating_mean"
]

seasons.columns = [
    "code",
    "title",
    "season_number",
    "season_rating_mean",
    "num_episodes"
]

episodes.columns = [
    "id_code",
    "season_number",
    "episode_number",
    "episode_rating",
    "code"
]


# Keep only required columns
seasons = seasons[
    ["code", "season_number", "season_rating_mean", "num_episodes"]
]


# Load data into SQLite
shows.to_sql(
    "shows",
    conn,
    if_exists="append",
    index=False
)

seasons.to_sql(
    "seasons",
    conn,
    if_exists="append",
    index=False
)

episodes.to_sql(
    "episodes",
    conn,
    if_exists="append",
    index=False
)


# Verify row counts
for table in ["shows", "seasons", "episodes"]:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(f"{table}: {count} rows")


conn.commit()
conn.close()

print("Data loaded successfully!")