import requests

url = 'http://localhost:5001/api/cards/create'
headers = {'Content-Type': 'application/json'}
data = {
    "note_type": "Basic",
    "deck_id": 1,
    "fields": {
        "Front": "What is the capital of France?",
        "Back": "Paris"
    },
    "tags": ["geography", "capitals"]
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Card created successfully:", response.json())
else:
    print("Failed to create card:", response.json())