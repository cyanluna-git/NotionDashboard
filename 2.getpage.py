import requests

TOKEN = "secret_duOD0wDCJn8pgrLcEasnRO5TOsOYu29hwikVYkBynoa"
WORKITEM_DB = "cfed17ffa07d4d52bfec6d9a46a8e92b"
MEMBER_DB = "9311c49e87c44fbf973d25995194808d"
PROJECT_DB = "0cdbad552f24482a808aaa388b1187c4"
VERSION_DB = "e5632cfff96048a4b6bd46ae014b3694"
KANBAN_DB = "0e43a41b7aeb4b0e968a2b472b77f911"



payload = {"page_size": 100}
headers = {
    "Authorization": "Bearer " + TOKEN,
    "Notion-Version": "2022-06-28",
    "content-type": "application/json"
}

def getDatabase(database, db_name):    
    url = f"https://api.notion.com/v1/databases/{database}/query"
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    import json
    with open( db_name + '.json','w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results

worktiems = getDatabase(WORKITEM_DB, 'workitem')
members = getDatabase(MEMBER_DB, 'member')
projects = getDatabase(PROJECT_DB, 'project')
versions = getDatabase(VERSION_DB, 'version')
kanbans = getDatabase(KANBAN_DB, 'kanban')

# for page in pages:
#     page_id = page["id"]
#     props = page["properties"]
#     title = props["Title"]
#     print(title)