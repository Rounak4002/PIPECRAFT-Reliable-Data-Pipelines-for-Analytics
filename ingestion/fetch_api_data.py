import requests
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["rates"].items(), columns=["currency", "rate"])
df["base_currency"] = data["base"]
df["date"] = data["date"]

df.to_csv("../data/raw/api_raw_data.csv", index=False)
print("Raw data ingested successfully.")
