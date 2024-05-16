import subprocess
import requests
from create_card import test_create_anki_card

# Initialize Anki with user profile "User 1"
subprocess.run(["curl", "-X", "POST", "http://localhost:5001/api/users/create/User%201"])

# Create a deck named "Hungarian"
subprocess.run(["curl", "-X", "POST", "http://localhost:5001/api/decks/create/Hungarian"])

# Run the script to create a card using requests
test_create_anki_card()

# Use requests to get cards from deck with ID 1 and save the IDs
response = requests.get("http://localhost:5001/api/decks/1/cards")
if response.status_code == 200:
    card_ids = [card['id'] for card in response.json()]
    print("Card IDs:", card_ids)

    # View contents of each card using the card IDs
    for card_id in card_ids:
        card_contents_response = requests.get(f"http://localhost:5001/api/cards/{card_id}/contents")
        if card_contents_response.status_code == 200:
            card_contents = card_contents_response.json()
            print(f"Card ID: {card_contents['id']}")
            print(f"Note ID: {card_contents['note_id']}")
            print(f"Deck ID: {card_contents['deck_id']}")
            print("Fields:")
            for field_name, field_content in card_contents['fields'].items():
                print(f"{field_name}: {field_content}")
            print()
        else:
            print(f"Failed to retrieve contents for card ID {card_id}: {card_contents_response.status_code}")
else:
    print("Failed to retrieve cards:", response.status_code)