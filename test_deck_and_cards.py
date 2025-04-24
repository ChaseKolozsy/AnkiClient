import sys
from src.operations.user_ops import create_user, delete_user
from src.operations.deck_ops import create_deck, get_decks, delete_deck, get_cards_in_deck
from src.operations.note_ops import get_notetypes
from src.operations.card_ops import create_card, get_card_contents


def main():
    username = "test_user"
    deck_name = "Test Deck"
    print(f"Creating user: {username}")
    user_resp = create_user(username)
    print("User response:", user_resp)

    # Check if deck exists and delete it
    print(f"Checking if deck '{deck_name}' exists for user '{username}'...")
    decks = get_decks(username)
    existing_deck_id = None
    if isinstance(decks, list):
        for deck in decks:
            if deck.get("name") == deck_name:
                existing_deck_id = deck.get("id")
                break
    if existing_deck_id:
        print(f"Deck '{deck_name}' exists (id={existing_deck_id}), deleting it...")
        del_resp = delete_deck(existing_deck_id, username)
        print("Delete deck response:", del_resp)

    print(f"Creating deck: {deck_name}")
    deck_resp = create_deck(deck_name, username)
    print("Deck response:", deck_resp)
    deck_id = deck_resp.get("id")
    if not deck_id:
        print("Failed to create deck. Exiting.")
        sys.exit(1)

    print(f"Fetching notetypes for user: {username}")
    notetypes = get_notetypes(username)
    print("Notetypes:", notetypes)
    if not notetypes or not isinstance(notetypes, list):
        print("No notetypes found. Exiting.")
        sys.exit(1)
    # Use 'Basic' notetype if available, else first
    notetype = next((nt for nt in notetypes if nt.get('name') == 'Basic'), notetypes[0])
    notetype_name = notetype['name']
    print(f"Using notetype: {notetype_name}")

    # Prepare card fields (assume 'Front' and 'Back' fields for Basic)
    fields_list = notetype.get('fields', ['Front', 'Back'])
    cards_to_create = [
        {fields_list[0]: "What is the capital of France?", fields_list[1]: "Paris"},
        {fields_list[0]: "What is 2+2?", fields_list[1]: "4"},
        {fields_list[0]: "What color is the sky?", fields_list[1]: "Blue"},
    ]

    print(f"Creating {len(cards_to_create)} cards...")
    for i, fields in enumerate(cards_to_create, 1):
        card_resp = create_card(
            username=username,
            note_type=notetype_name,
            deck_id=deck_id,
            fields=fields,
            tags=["test"]
        )
        print(f"Card {i} response:", card_resp)

    print(f"Listing cards in deck {deck_id}...")
    cards_list = get_cards_in_deck(deck_id, username)
    print("Cards in deck:", cards_list)

    # Retrieve and display contents of each card
    if isinstance(cards_list, list):
        print("\nCard contents:")
        for card in cards_list:
            card_id = card.get("id")
            if card_id is not None:
                contents = get_card_contents(card_id=card_id, username=username)
                print(f"Card ID {card_id} contents:", contents)

if __name__ == "__main__":
    main() 