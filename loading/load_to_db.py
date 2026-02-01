import pandas as pd
import mysql.connector
from config.db_config import DB_CONFIG

df = pd.read_csv("../data/processed/cleaned_data.csv")

conn = mysql.connector.connect(
    host=DB_CONFIG["host"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    database=DB_CONFIG["database"]
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exchange_rates (
    currency VARCHAR(10),
    rate FLOAT,
    base_currency VARCHAR(10),
    date DATE
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO exchange_rates VALUES (%s, %s, %s, %s)",
        tuple(row)
    )

conn.commit()
conn.close()

print("Data loaded into database successfully.")
