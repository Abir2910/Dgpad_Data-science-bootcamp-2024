import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['AlMayadeen']
collection = db['articles']

# List of JSON files
json_files = [
    'output/articles_2024_03.json',
    'output/articles_2024_04.json',
    'output/articles_2024_05.json',
    'output/articles_2024_06.json',
    'output/articles_2024_07.json',
    'output/articles_2024_08.json',
    # Add more files if needed
]

# Load each JSON file and insert into MongoDB
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        collection.insert_many(data)

print("All data inserted successfully.")


