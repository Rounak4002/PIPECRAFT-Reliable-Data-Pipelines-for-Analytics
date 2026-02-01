import pandas as pd

df = pd.read_csv("../data/raw/api_raw_data.csv")

df = df.drop_duplicates()
df = df[df["rate"] > 0]

df["rate"] = df["rate"].round(4)

df.to_csv("../data/processed/cleaned_data.csv", index=False)
print("Data cleaned and transformed successfully.")
