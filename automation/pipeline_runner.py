import os

os.system("python ingestion/fetch_api_data.py")
os.system("python transformation/clean_transform.py")
os.system("python loading/load_to_db.py")

print("PIPECRAFT pipeline executed successfully.")
