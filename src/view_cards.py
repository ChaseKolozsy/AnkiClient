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
                print(f"Queue: {card_contents['queue']}")
                print("Fields:")
                for field_name, field_content in card_contents['fields'].items():
                    print(f"{field_name}: {field_content}")
                print()
            else:
                print(f"Failed to retrieve contents for card ID {card_id}: {card_contents_response.status_code}")
    else:
        print("Failed to retrieve cards:", response.status_code)

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

if __name__ == "__main__":
    choice = input("view cards in deck: 1, view cards by tag: 2, view cards by state: 3, view cards by tag and state: 4, ")
    if choice == "1":
        deck_number = input("Enter the deck number: ")
        view_deck_cards(deck_number)
    elif choice == "2":
        tag = input("Enter the tag: ")
        view_cards_by_tag(tag)
    elif choice == "3":
        deck_id = input("Enter the deck id: ")
        state = input("Enter the state (new, learning, due, suspended, manually_buried, sibling_buried, day_learn_relearn, preview): ")
        view_by_state(deck_id, state)
    elif choice == "4":
        tag = input("Enter the tag: ")
        state = input("Enter the state (new, learning, due, suspended, manually_buried, sibling_buried, day_learn_relearn, preview): ")
        view_by_tag_and_state(tag, state)