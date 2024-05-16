import requests
from pathlib import Path
import json

def view_deck_cards(deck_id):
    response = requests.get(f"http://localhost:5001/api/decks/{deck_id}/cards")
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

deck_number = input("Enter the deck number: ")
view_deck_cards(deck_number)

