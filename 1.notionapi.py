import requests

TOKEN = "secret_duOD0wDCJn8pgrLcEasnRO5TOsOYu29hwikVYkBynoa"
DATABASE_ID = "cfed17ffa07d4d52bfec6d9a46a8e92b"

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

payload = {"page_size": 100}
headers = {
    "Authorization": "Bearer " + TOKEN,
    "Notion-Version": "2022-06-28",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text) 