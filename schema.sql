DROP TABLE IF EXISTS episodes;
DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS shows;


CREATE TABLE shows (

    code TEXT PRIMARY KEY,

    title TEXT,

    rating REAL,

    rating_count INTEGER,

    rank INTEGER,

    rating_mean REAL

);


CREATE TABLE seasons (

    code TEXT,

    season_number INTEGER,

    season_rating_mean REAL,

    num_episodes INTEGER,

    PRIMARY KEY (code, season_number),

    FOREIGN KEY(code)
        REFERENCES shows(code)

);


CREATE TABLE episodes (

    id_code INTEGER,

    code TEXT,

    season_number INTEGER,

    episode_number INTEGER,

    episode_rating REAL,

    PRIMARY KEY (
        code,
        season_number,
        episode_number
    ),

    FOREIGN KEY(code)
        REFERENCES shows(code)

);