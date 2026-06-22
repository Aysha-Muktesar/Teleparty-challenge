import sqlite3
import pandas as pd

conn = sqlite3.connect("teleparty.db")


def run_query(query, title):

    print("\n")
    print("="*60)
    print(title)
    print("="*60)

    df = pd.read_sql_query(query, conn)

    print(df)



##############################################
# Report 1
##############################################

query1 = """

SELECT title,
       rating

FROM shows

WHERE rating<=6

"""


run_query(
    query1,
    "Shows with Rating <= 6"
)



##############################################
# Report 2
##############################################

query2 = """

SELECT s.title,

COUNT(*) seasons


FROM shows s

JOIN seasons se

ON s.code=se.code


GROUP BY s.title


HAVING COUNT(*)>1


ORDER BY seasons DESC


"""


run_query(
    query2,
    "Shows Having More Than One Season"
)




##############################################
# Report 3
##############################################

query3 = """

WITH temp AS (

SELECT *
FROM shows

WHERE rating_count = (
    SELECT MAX(rating_count)
    FROM shows
)

)

SELECT

title,

rating_count,

rank,

(
SELECT COUNT(*)
FROM episodes e
WHERE e.code = temp.code
) AS episodes,

(
SELECT COUNT(*)
FROM seasons s
WHERE s.code = temp.code
) AS seasons

FROM temp

WHERE rank = (
SELECT MIN(rank)
FROM temp
)


"""


run_query(
    query3,
    "Highest Rating Count and Lowest Rank"
)




##############################################
# Report 4
##############################################

query4 = """

WITH temp AS (

SELECT *
FROM shows

WHERE rating_count = (
    SELECT MIN(rating_count)
    FROM shows
)

)

SELECT

title,

rating_count,

rank,

(
SELECT COUNT(*)
FROM episodes e
WHERE e.code = temp.code
) AS episodes,

(
SELECT COUNT(*)
FROM seasons s
WHERE s.code = temp.code
) AS seasons

FROM temp

WHERE rank = (
SELECT MAX(rank)
FROM temp
)


"""


run_query(
    query4,
    "Lowest Rating Count and Highest Rank"
)



conn.close()
