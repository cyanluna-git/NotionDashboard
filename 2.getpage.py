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
def getPages():
    
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    import json
    with open('db.json','w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results

pages = getPages()

for page in pages:
    page_id = page["id"]
    props = page["properties"]
    title = props["Title"]
    print(title)