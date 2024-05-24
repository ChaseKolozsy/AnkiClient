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

def get_cards_by_tag(*, tag: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/by-tag"
    data = {
        "tag": tag,
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_state(*, deck_id: int, state: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/{deck_id}/by-state"
    data = {
        "state": state,
        "username": username
    }
    response = requests.get(url, json=data)
    return response.json()

def get_cards_by_tag_and_state(*, tag: str, state: str, username: str) -> Dict[str, Any]:
    url = f"{BASE_URL}/by-tag-and-state"
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


if __name__ == "__main__":
    import note_ops

    notetypes = note_ops.get_notetypes()
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

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

    print("\n\n-------------------------------------------\n\n")

    response = change_card_notetype(note_id=card_id, username="User 1", new_notetype_id=notetype_dict["Basic (type in the answer)"], match_by_name=False)
    print(response, '\n\n')

    response = get_card_contents(card_id=card_id, username="User 1")
    print(response, '\n\n')

    response = change_notetype_by_tag(tag="geography", new_notetype_id=notetype_dict["Basic (type in the answer)"], username="User 1", match_by_name=True)
    print(response, '\n\n')

    response = change_notetype_by_current(current_notetype_id=notetype_dict["Basic (type in the answer)"], new_notetype_id=notetype_dict["Basic"], username="User 1", match_by_name=True)
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    print(f"status: {response}")
    for card in response:
        print(card['id'])
    card_ids = [int(card['id']) for card in response]

    response = move_cards(card_ids=card_ids, target_deck_name="Hungarian", username="User 1")
    print(response, '\n\n')

    response = delete_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    response = delete_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Norway?", "Back": "Oslo"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Denmark?", "Back": "Copenhagen"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Germany?", "Back": "Berlin"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of France?", "Back": "Paris"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Spain?", "Back": "Madrid"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Italy?", "Back": "Rome"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of UK?", "Back": "London"}, tags=["geography", "capitals"])
    response = create_card(username="User 1", note_type="Basic", deck_id=1, fields={"Front": "What is the capital of Sweden?", "Back": "Stockholm"}, tags=["geography", "capitals"])

    response = delete_cards_by_deck(deck="1", username="User 1")
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    print(f"status: {response}")
    if len(response) > 0:
        for card in response:
            print(card['id'])
    else:
        print("No cards to delete")

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

    response = reschedule_card(card_id=card_id, new_due_date="7", username="User 1")
    print(response, '\n\n')

    response = reschedule_cards_by_tag(tag="geography", username="User 1", start_days=7, end_days=21, only_if_due=False)
    print(response, '\n\n')

    response = reschedule_cards_by_deck(deck_id=1, username="User 1", start_days=9, end_days=27, only_if_due=False)
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    response = get_cards_by_state(deck_id=1, state="due", username="User 1")
    print(response, '\n\n')

    print("\n\n-------------------------------------------\n\n")

    response = reset_card(card_id=card_id)
    print(response, '\n\n')

    response = reset_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    response = reset_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    response = reposition_card(card_id=card_id, new_position=99, username="User 1")
    print(response, '\n\n')

    response = reposition_cards_by_tag(tag="geography", new_position=1, username="User 1")
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    response = reposition_cards_by_deck(deck_id=1, new_position=1000, username="User 1")
    print(response, '\n\n') 
    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    response = suspend_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    response = suspend_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    response = suspend_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    response = bury_card(card_id=card_id, username="User 1")
    print(response, '\n\n')

    response = bury_cards_by_tag(tag="geography", username="User 1")
    print(response, '\n\n')

    response = bury_cards_by_deck(deck_id=1, username="User 1")
    print(response, '\n\n')

    response = get_cards_by_tag(tag="geography", username="User 1")
    for card in response:
        print(card)

    response = delete_cards_by_deck(deck="1", username="User 1")
    print(response, '\n\n')