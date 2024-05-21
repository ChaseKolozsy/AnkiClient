import requests

def view_cards_by_tag(tag):
    response = requests.get(f"http://localhost:5001/api/cards/by-tag?tag={tag}")
    if response.status_code == 200:
        cards = response.json()
        print(cards)
    else:
        print("Failed to retrieve cards:", response.status_code)

def view_by_state(deck_id, state):
    response = requests.get(f"http://localhost:5001/api/cards/{deck_id}/by-state?state={state}")
    if response.status_code == 200:
        cards = response.json()
        print(cards)
    else:
        print("Failed to retrieve cards by state:", response.json()['error'], response.status_code)

def view_by_tag_and_state(tag, state):
    response = requests.get(f"http://localhost:5001/api/cards/by-tag-and-state?tag={tag}&state={state}")
    if response.status_code == 200:
        cards_by_tag = response.json()[0]
        cards_by_state = response.json()[1]
        print(cards_by_tag)
        print(cards_by_state)
        print(f'len(cards_by_tag): {len(cards_by_tag)}, len(cards_by_state): {len(cards_by_state)}')
    else:
        print("Failed to retrieve cards by tag and state:", response.json()['error'], response.status_code)

def create_anki_card():
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