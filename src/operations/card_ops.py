import requests
from typing import List, Dict, Any, Optional

BASE_URL = "http://localhost:5001/api/cards"

def create_card(*, username: str, note_type: str, deck_id: int, fields: Dict[str, str], tags: Optional[List[str]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/create"
    data = {
        "username": username,
        "note_type": note_type,
        "deck_id": deck_id,
        "fields": fields,
        "tags": tags or []
    }
    response = requests.post(url, json=data)
    return response.json()

def change_card_notetype(*, note_id: int, username: str, new_notetype_id: int, match_by_name: bool = True) -> Dict[str, Any]:
    url = f"{BASE_URL}/{note_id}/change-notetype"
    data = {
        "username": username,
        "new_notetype_id": new_notetype_id,
        "match_by_name": match_by_name
    }
    response = requests.post(url, json=data)
    return response.json()

def change_notetype_by_tag(*, tag: str, new_notetype_id: int, username: str, match_by_name: bool = True) -> Dict[str, Any]:
    url = f"{BASE_URL}/change-notetype-by-tag"
    data = {
        "tag": tag,
        "new_notetype_id": new_notetype_id,
        "match_by_name": match_by_name,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def change_notetype_by_current(*, current_notetype_id: int, new_notetype_id: int, username: str, match_by_name: bool = True) -> Dict[str, Any]:
    url = f"{BASE_URL}/change-notetype-by-current"
    data = {
        "current_notetype_id": current_notetype_id,
        "new_notetype_id": new_notetype_id,
        "match_by_name": match_by_name,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def move_cards(*, card_ids: List[int], target_deck_name: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/move-cards"
    data = {
        "card_ids": card_ids,
        "target_deck_name": target_deck_name,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reschedule_card(*, card_id: int, new_due_date: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/reschedule"
    data = {
        "new_due_date": new_due_date,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reschedule_cards_by_tag(*, tag: str, username: str, new_due_date: Optional[str] = None, start_days: Optional[int] = None, end_days: Optional[int] = None, only_if_due: bool = False) -> Dict[str, Any]:
    url = f"{BASE_URL}/reschedule/by-tag"
    data = {
        "tag": tag,
        "new_due_date": new_due_date,
        "start_days": start_days,
        "end_days": end_days,
        "only_if_due": only_if_due,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reschedule_cards_by_deck(*, deck_id: int, username: str, new_due_date: Optional[str] = None, start_days: Optional[int] = None, end_days: Optional[int] = None, only_if_due: bool = False) -> Dict[str, Any]:
    url = f"{BASE_URL}/reschedule/by-deck"
    data = {
        "deck_id": deck_id,
        "new_due_date": new_due_date,
        "start_days": start_days,
        "end_days": end_days,
        "only_if_due": only_if_due,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reposition_card(*, card_id: int, new_position: int, username: str, increment_collection: bool = False, randomize: bool = False) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/reposition"
    data = {
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reposition_cards_by_tag(*, tag: str, new_position: int, username: str, increment_collection: bool = False, randomize: bool = False) -> Dict[str, Any]:
    url = f"{BASE_URL}/reposition/by-tag"
    data = {
        "tag": tag,
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reposition_cards_by_deck(*, deck_id: int, new_position: int, username: str, increment_collection: bool = False, randomize: bool = False) -> Dict[str, Any]:
    url = f"{BASE_URL}/reposition/by-deck"
    data = {
        "deck_id": deck_id,
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reset_card(*, card_id: int) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/reset"
    response = requests.post(url)
    return response.json()

def reset_cards_by_tag(*, tag: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/reset/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def reset_cards_by_deck(*, deck_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/reset/by-deck"
    data = {
        "deck_id": deck_id,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def suspend_card(*, card_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/suspend"
    data = {
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def suspend_cards_by_tag(*, tag: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/suspend/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def suspend_cards_by_deck(*, deck_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/suspend/by-deck"
    data = {
        "deck_id": deck_id,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def bury_card(*, card_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/bury"
    data = {
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def bury_cards_by_tag(*, tag: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/bury/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def bury_cards_by_deck(*, deck_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/bury/by-deck"
    data = {
        "deck_id": deck_id,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def get_card_contents(*, card_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{card_id}/contents"
    data = {
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def get_card_by_id(*, note_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{note_id}"
    data = {
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_tag(*, tag: str, username: str, inclusions: Optional[list] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_state(*, deck_id: int, state: str, username: str, inclusions: Optional[list] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/{deck_id}/by-state"
    data = {
        "state": state,
        "username": username
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_state_without_fields(*, deck_id: int, state: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{deck_id}/by-state-without-fields"
    data = {
        "state": state,
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_tag_and_state(*, tag: str, state: str, username: str, inclusions: Optional[list] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}/by-tag-and-state"
    data = {
        "tag": tag,
        "state": state,
        "username": username
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_tag_and_state_without_fields(*, tag: str, state: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/by-tag-and-state-without-fields"
    data = {
        "tag": tag,
        "state": state,
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def delete_card(*, card_id: int, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/delete/{card_id}"
    data = {
        "username": username
    }
    response = requests.delete(url, json=data)
    return response.json()

def delete_cards_by_tag(*, tag: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/delete/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    response = requests.delete(url, json=data)
    return response.json()

def delete_cards_by_deck(*, deck: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/delete/by-deck"
    data = {
        "deck": deck,
        "username": username
    }
    response = requests.delete(url, json=data)
    return response.json()

def get_cards_by_ease_(*, username: str, deck_id: int, min_reviews: int = 3, min_factor: int = 2000, max_factor: int = 2750, min_ratio: float = 0.2, max_ratio: float = 1.0, include_suspended: bool = False, include_fields: bool = True, inclusions: Optional[list] = None) -> Dict[str, Any]:
    url = f'{BASE_URL}/by-ease'
    data = {
        'username': username,
        'deck_id': deck_id,
        'min_reviews': min_reviews,
        'min_factor': min_factor,
        'max_factor': max_factor,
        'min_ratio': min_ratio,
        'max_ratio': max_ratio,
        'include_suspended': include_suspended,
        'include_fields': include_fields
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_learning_metrics(*, username: str, deck_id: int, min_reviews: Optional[int] = None, max_reviews: Optional[int] = None, min_interval: Optional[int] = None, max_interval: Optional[int] = None, min_factor: Optional[int] = None, max_factor: Optional[int] = None, min_lapses: Optional[int] = None, max_lapses: Optional[int] = None, min_ratio: Optional[float] = None, max_ratio: Optional[float] = None, include_suspended: bool = False, include_new: bool = False, include_fields: bool = True, limit: int = 100, inclusions: Optional[list] = None) -> Dict[str, Any]:
    url = f'{BASE_URL}/by-learning-metrics'
    data = {
        'username': username,
        'deck_id': deck_id,
        'min_reviews': min_reviews,
        'max_reviews': max_reviews,
        'min_interval': min_interval,
        'max_interval': max_interval,
        'min_factor': min_factor,
        'max_factor': max_factor,
        'min_lapses': min_lapses,
        'max_lapses': max_lapses,
        'min_ratio': min_ratio,
        'max_ratio': max_ratio,
        'include_suspended': include_suspended,
        'include_new': include_new,
        'include_fields': include_fields,
        'limit': limit
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    response = requests.get(url, json=data)
    return response.json()

def reset_difficult_cards(*, username: str, deck_id: int, min_reviews: int = 5, max_factor: int = 1800, min_ratio: float = 0.3, min_lapses: int = 3) -> Dict[str, Any]:
    url = f'{BASE_URL}/reset-difficult'
    data = {
        'username': username,
        'deck_id': deck_id,
        'min_reviews': min_reviews,
        'max_factor': max_factor,
        'min_ratio': min_ratio,
        'min_lapses': min_lapses
    }
    response = requests.post(url, json=data)
    return response.json()

def get_cards_by_note_id(*, note_id: int, username: str, inclusions: Optional[list] = None) -> Dict[str, Any]:
    """Get all cards associated with a specific note ID.
    
    Args:
        note_id: The ID of the note to retrieve cards for
        username: The username of the Anki user
        inclusions: Optional list of specific fields to include in the response
        
    Returns:
        A list of cards associated with the note ID
    """
    url = f"{BASE_URL}/by-note-id/{note_id}"
    data = {
        "username": username
    }
    if inclusions is not None:
        data["inclusions"] = inclusions
    
    try:
        response = requests.get(url, json=data)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.json()
    except requests.exceptions.JSONDecodeError:
        # Handle empty responses
        if response.status_code == 200 and not response.text:
            return []
        # Re-raise the exception for other JSON decode errors
        raise
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        return {"error": str(e)}


def test_card_ops():
    from note_ops import get_notetypes
    from user_ops import create_user, delete_user
    from deck_ops import create_deck
    from import_ops import upload_anki_package, upload_csv_file
    from pathlib import Path

    ## ----------------------------------- Initialize ------------------------------------- ##
    username = "User 1"  # Replace with the actual username
    print(create_user(username))
    deck_id = create_deck(deck_name="testdeck", username=username)['id']
    print(deck_id)
    create_deck(deck_name="Hungarian", username=username)

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'Hungarian'
    delimiter = 'TAB'

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)



    notetypes = get_notetypes(username)
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

    ## ----------------------------------- Test Cards ------------------------------------- ##

    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Norway?", "Back": "Oslo"}, tags=["geography", "capitals"])
    print(response, '\n\n')
    if response.get('card_ids'):
        card_id = response['card_ids'][0]
        print(response['note_id'], response['card_ids'][0])
    else:
        print("Failed to create card")
    card = get_card_by_id(note_id=response['card_ids'][0], username="User 1")
    print(card, '\n\n')

    print("\n\n-------------- Contents ------------------------\n\n")

    response = get_card_contents(card_id=card_id, username="User 1")
    print(response, '\n\n')

    print("\n\n-------------- By Tag and State ------------------------\n\n")

    response = get_cards_by_tag_and_state(tag="Food", state="due", username="User 1")
    print(response, '\n\n')

    print("\n\n-------------- By Tag and State ------------------------\n\n")

    response = get_cards_by_tag_and_state(tag="Food", state="new", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Change card notetype ---------------------------\n\n")

    response = change_card_notetype(note_id=card_id, username="User 1", new_notetype_id=notetype_dict["Basic (type in the answer)"], match_by_name=False)
    print(response, '\n\n')
    
    print("\n\n---------------- Get card contents ---------------------------\n\n")

    response = get_card_contents(card_id=card_id, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Change notetype by tag ---------------------------\n\n")

    response = change_notetype_by_tag(tag="geography", new_notetype_id=notetype_dict["Basic (type in the answer)"], username="User 1", match_by_name=True)
    print(response, '\n\n')

    print("\n\n---------------- Change notetype by deck ---------------------------\n\n")

    response = change_notetype_by_current(current_notetype_id=notetype_dict["Basic (type in the answer)"], new_notetype_id=notetype_dict["Basic"], username="User 1", match_by_name=True)
    print(response, '\n\n')

    print("\n\n---------------- Get cards by tag ---------------------------\n\n")

    response = get_cards_by_tag(tag="geography", username="User 1")
    print(f"status: {response}")
    for card in response:
        print(card['id'])
    card_ids = [int(card['id']) for card in response]

    print("\n\n---------------- Move cards ---------------------------\n\n")

    response = move_cards(card_ids=card_ids, target_deck_name="Hungarian", username=username)
    print(response, '\n\n')

    print("\n\n---------------- Delete card ---------------------------\n\n")

    response = delete_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Delete cards by tag ---------------------------\n\n")

    response = delete_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Create cards ---------------------------\n\n")

    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Norway?", "Back": "Oslo"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Denmark?", "Back": "Copenhagen"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Germany?", "Back": "Berlin"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of France?", "Back": "Paris"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Spain?", "Back": "Madrid"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Italy?", "Back": "Rome"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of UK?", "Back": "London"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Sweden?", "Back": "Stockholm"}, tags=["geography", "capitals"])

    print("\n\n---------------- Delete cards by deck ---------------------------\n\n")

    response = delete_cards_by_deck(deck="1", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Get cards by tag ---------------------------\n\n")

    response = get_cards_by_tag(tag="geography", username="User 1")
    print(f"status: {response}")
    if len(response) > 0:
        for card in response:
            print(card['id'])
    else:
        print("No cards to delete")

    print("\n\n---------------- Create cards ---------------------------\n\n")

    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Norway?", "Back": "Oslo"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Denmark?", "Back": "Copenhagen"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Germany?", "Back": "Berlin"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of France?", "Back": "Paris"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Spain?", "Back": "Madrid"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Italy?", "Back": "Rome"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of UK?", "Back": "London"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Sweden?", "Back": "Stockholm"}, tags=["geography", "capitals"])

    if response.get('card_ids'):
        card_id = response['card_ids'][0]
    else:
        print("Failed to create cards")

    print("\n\n---------------- Reschedule card ---------------------------\n\n")

    response = reschedule_card(card_id=card_id, new_due_date="7", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reschedule cards by tag ---------------------------\n\n")

    response = reschedule_cards_by_tag(tag="geography", username="User 1", start_days=7, end_days=21, only_if_due=False)
    print(response, '\n\n')

    print("\n\n---------------- Reschedule cards by deck ---------------------------\n\n")

    response = reschedule_cards_by_deck(deck_id=1, username="User 1", start_days=9, end_days=27, only_if_due=False)
    print(response, '\n\n')

    print("\n\n---------------- Get cards by tag ---------------------------\n\n")

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    print("\n\n---------------- Get cards by state ---------------------------\n\n")

    response = get_cards_by_state(deck_id=1, state="due", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reset card ---------------------------\n\n")

    response = reset_card(card_id=card_id)
    print(response, '\n\n')

    print("\n\n---------------- Reset cards by tag ---------------------------\n\n")

    response = reset_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reset cards by deck ---------------------------\n\n")

    response = reset_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reposition card ---------------------------\n\n")

    response = reposition_card(card_id=card_id, new_position=99, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reposition cards by tag ---------------------------\n\n")

    response = reposition_cards_by_tag(tag="geography", new_position=1, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Reposition cards by deck ---------------------------\n\n")

    response = reposition_cards_by_deck(deck_id=1, new_position=1000, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Get Cards by tag ---------------------------\n\n")

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    print("\n\n---------------- Reposition cards by deck ---------------------------\n\n")

    response = reposition_cards_by_deck(deck_id=1, new_position=1000, username="User 1")
    print(response, '\n\n') 
    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    print("\n\n---------------- Suspend card ---------------------------\n\n")
    response = suspend_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Suspend cards by tag ---------------------------\n\n")
    response = suspend_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Suspend cards by deck ---------------------------\n\n")
    response = suspend_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Get cards by tag ---------------------------\n\n")
    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    print("\n\n---------------- Bury card ---------------------------\n\n")
    response = bury_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Bury cards by tag ---------------------------\n\n")
    response = bury_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Bury cards by deck ---------------------------\n\n")
    response = bury_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    print("\n\n---------------- Delete cards by deck ---------------------------\n\n")
    response = delete_cards_by_deck(deck="1", username="User 1")
    print(response, '\n\n')


    delete_user(username)

#if __name__ == "__main__":
#    import json
#    username = 'chase'
#    deck_id = "1745682159947"
#    #response = get_cards_by_tag_and_state_without_fields(tag="Chapter_30", state="new", username=username)
#    #print(json.dumps(response, indent=4, ensure_ascii=False))
#    print("\n\n---------------- Get cards by learning metrics ---------------------------\n\n")
#    response = get_cards_by_learning_metrics(
#        username=username,
#        deck_id=deck_id,
#        min_reviews=0,
#        max_reviews=8,
#        min_interval=4,
#        max_interval=6,
#        include_suspended=False,
#        include_new=False,
#        include_fields=True,
#        limit=10
#    )
#    print(json.dumps(response, indent=4, ensure_ascii=False))
#
#    #print("\n\n---------------- get difficult cards ---------------------------\n\n")
#    #response = get_cards_by_ease_(
#    #    username=username,
#    #    deck_id=deck_id,
#    #    min_reviews=8,
#    #    max_factor=2300,
#    #    min_ratio=2.0,
#    #    include_suspended=False,
#    #    include_fields=True
#    #)
#    #print(json.dumps(response, indent=4, ensure_ascii=False))



if __name__ == "__main__":
    import json
    username = "chase"
    
    # Test getting cards by note ID
    note_id = 1745675387205  # Note ID from the error
    print(f"\nTesting get_cards_by_note_id with note_id={note_id}")
    try:
        response = get_cards_by_note_id(note_id=note_id, username=username)
        print(json.dumps(response, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Error testing get_cards_by_note_id: {e}")
    