import os
import psycopg2
from dotenv import load_dotenv, find_dotenv
from solution import individual_colors
from collections import Counter

load_dotenv(find_dotenv())


# six
# Connect to the database
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS colors (
        color VARCHAR(255),
        frequency INTEGER
        );
    """)

# conn.commit()


color_frequency = Counter(individual_colors)


for color, frequency in color_frequency.items():

    # cur = conn.cursor()

    cur.execute("""
        INSERT INTO colors (color, frequency) VALUES (%s, %s);
        """, (color, frequency))

conn.commit()

cur.close()
conn.close()

print("Table created successfully")



