import subprocess
import requests
from create_card import test_create_anki_card
from import_decks import upload_csv_file, upload_anki_package
from pathlib import Path

def create_deck_and_get_id(deck_name):
    response = requests.post(f"http://localhost:5001/api/decks/create/{deck_name}")
    if response.status_code == 201:
        deck_data = response.json()
        return deck_data.get("id")
    return None

# Example usageg
# Initialize Anki with user profile "User 1"
subprocess.run(["curl", "-X", "POST", "http://localhost:5001/api/users/create/User%201"])


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

if __name__ == "__main__":
    username = "User 1"

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    deck_id = create_deck_and_get_id("Hungarian")
    notetype = 'Basic' 
    deck_name = 'Hungarian'
    delimiter = 'TAB'
    print(deck_id)

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)


