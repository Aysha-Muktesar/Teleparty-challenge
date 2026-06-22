# Teleparty-challenge
Take home assignment 


## Project Structure
teleparty-challenge/
│── data/
│── docs/
│── schema.sql
│── load_data.py
│── reports.py
│── requirements.txt
│── README.md

## OBSERVATIONS:

1. During ingestion, I discovered that id_code in all-episode-ratings.csv was not globally unique (16,322 duplicates). I therefore replaced the surrogate key with a composite primary key (code, season_number, episode_number), which correctly models the natural uniqueness of an episode.

2. The dataset contains no shows with rating ≤ 6 (minimum rating observed: 8.3), therefore Report 1 correctly returns an empty result set.

