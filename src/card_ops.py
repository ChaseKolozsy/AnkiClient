import requests
from notes_ops import *

def create_anki_card(note_type, deck_id, fields, tags=[]):
    """TESTED"""
    url = 'http://localhost:5001/api/cards/create'
    headers = {'Content-Type': 'application/json'}
    data = {
        "note_type": note_type,
        "deck_id": deck_id,
        "fields": fields,
        "tags": tags
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def change_card_notetype(card_id, new_notetype_id, match_by_name=True):
    """TESTED"""
    url = f'http://localhost:5001/api/cards/{card_id}/change-notetype'
    headers = {'Content-Type': 'application/json'}
    data = {"new_notetype_id": new_notetype_id, "match_by_name": match_by_name}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def change_notetype_by_tag(tag, new_notetype_id, match_by_name=True):
    """TESTED"""
    url = 'http://localhost:5001/api/cards/change-notetype-by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {"tag": tag, "new_notetype_id": new_notetype_id, "match_by_name": match_by_name}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def change_notetype_by_current(current_notetype_id, new_notetype_id, match_by_name=True):
    """TESTED"""
    url = 'http://localhost:5001/api/cards/change-notetype-by-current'
    headers = {'Content-Type': 'application/json'}
    data = {"current_notetype_id": current_notetype_id, "new_notetype_id": new_notetype_id, "match_by_name": match_by_name}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def move_cards(card_ids, target_deck_name, username):
    """TESTED"""
    url = 'http://localhost:5001/api/move-cards'
    headers = {'Content-Type': 'application/json'}
    data = {"card_ids": card_ids, "target_deck_name": target_deck_name, "username": username}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reschedule_card(card_id, new_due_date):
    url = f'http://localhost:5001/api/cards/{card_id}/reschedule'
    headers = {'Content-Type': 'application/json'}
    data = {"new_due_date": new_due_date}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reschedule_cards_by_tag(tag, new_due_date=None, start_days=None, end_days=None, only_if_due=False):
    url = 'http://localhost:5001/api/cards/reschedule/by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {"tag": tag, "new_due_date": new_due_date, "start_days": start_days, "end_days": end_days, "only_if_due": only_if_due}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reschedule_cards_by_deck(deck_id, new_due_date=None, start_days=None, end_days=None, only_if_due=False):
    url = 'http://localhost:5001/api/cards/reschedule/by-deck'
    headers = {'Content-Type': 'application/json'}
    data = {"deck_id": deck_id, "new_due_date": new_due_date, "start_days": start_days, "end_days": end_days, "only_if_due": only_if_due}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reposition_card(card_id, new_position, increment_collection=False, randomize=False):
    url = f'http://localhost:5001/api/cards/{card_id}/reposition'
    headers = {'Content-Type': 'application/json'}
    data = {
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reposition_cards_by_tag(tag, new_position, increment_collection=False, randomize=False):
    url = 'http://localhost:5001/api/cards/reposition/by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {
        "tag": tag,
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reposition_cards_by_deck(deck_id, new_position, increment_collection=False, randomize=False):
    url = 'http://localhost:5001/api/cards/reposition/by-deck'
    headers = {'Content-Type': 'application/json'}
    data = {
        "deck_id": deck_id,
        "new_position": new_position,
        "increment_collection": increment_collection,
        "randomize": randomize
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reset_card(card_id):
    url = f'http://localhost:5001/api/cards/{card_id}/reset'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reset_cards_by_tag(tag):
    url = 'http://localhost:5001/api/cards/reset/by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {"tag": tag}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def reset_cards_by_deck(deck_id):
    url = 'http://localhost:5001/api/cards/reset/by-deck'
    headers = {'Content-Type': 'application/json'}
    data = {"deck_id": deck_id}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(e)
        return None

def suspend_card(card_id):
    url = f'http://localhost:5001/api/cards/{card_id}/suspend'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def suspend_cards_by_tag(tag):
    url = 'http://localhost:5001/api/cards/suspend/by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {"tag": tag}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def suspend_cards_by_deck(deck_id):
    url = 'http://localhost:5001/api/cards/suspend/by-deck'
    headers = {'Content-Type': 'application/json'}
    data = {"deck_id": deck_id}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def bury_card(card_id):
    url = f'http://localhost:5001/api/cards/{card_id}/bury'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def bury_cards_by_tag(tag):
    url = 'http://localhost:5001/api/cards/bury/by-tag'
    headers = {'Content-Type': 'application/json'}
    data = {"tag": tag}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def bury_cards_by_deck(deck_id):
    url = 'http://localhost:5001/api/cards/bury/by-deck'
    headers = {'Content-Type': 'application/json'}
    data = {"deck_id": deck_id}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def get_card_contents(card_id):
    url = f'http://localhost:5001/api/cards/{card_id}/contents'
    try:
        response = requests.get(url)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def get_card_by_id(card_id):
    """TESTED"""
    url = f'http://localhost:5001/api/cards/{card_id}'
    try:
        response = requests.get(url)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def get_cards_by_tag(tag):
    """TESTED"""
    url = 'http://localhost:5001/api/cards/by-tag'
    params = {"tag": tag}
    try:
        response = requests.get(url, params=params)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def get_cards_by_state(deck_id, state):
    url = f'http://localhost:5001/api/cards/{deck_id}/by-state'
    params = {"state": state}
    try:
        response = requests.get(url, params=params)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def get_cards_by_tag_and_state(tag, state):
    url = 'http://localhost:5001/api/cards/by-tag-and-state'
    params = {"tag": tag, "state": state}
    try:
        response = requests.get(url, params=params)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def delete_card(card_id):
    url = f'http://localhost:5001/api/cards/delete/{card_id}'
    try:
        response = requests.delete(url)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def delete_cards_by_tag(tag):
    url = 'http://localhost:5001/api/cards/delete/by-tag'
    params = {"tag": tag}
    try:
        response = requests.delete(url, params=params)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

def delete_cards_by_deck(deck_identifier):
    url = 'http://localhost:5001/api/cards/delete/by-deck'
    params = {"deck": deck_identifier}
    try:
        response = requests.delete(url, params=params)
        return response.json(), response.status_code
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    notetypes = get_notetypes()
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

    response, status = create_anki_card("Basic", 1, {"Front": "What is the capital of Norway?", "Back": "Oslo"}, ["geography", "capitals"])
    print(response, status, '\n\n')
    if status == 201:
        card_id = response['card_ids'][0]
        print(response['note_id'], response['card_ids'][0])
    else:
        print("Failed to create card")
    card = get_card_by_id(response['card_ids'][0])
    print(card, '\n\n')

    response, status = change_card_notetype(response['note_id'], notetype_dict["Basic (type in the answer)"], False)
    print(response, status, '\n\n')

    notetype_id = get_notetype_id_by_card_id(card_id)
    print(notetype_id, '\n\n')

    response, status = get_card_contents(card_id)
    print(response, status, '\n\n')

    response, status = change_notetype_by_tag("geography", notetype_dict["Basic (type in the answer)"], True)
    print(response, status, '\n\n')

    response = change_notetype_by_current(notetype_dict["Basic (type in the answer)"], notetype_dict["Basic"], True)
    print(response, '\n\n')

    response, status = get_cards_by_tag("geography")
    print(f"status: {status}")
    for card in response:
        print(card['id'])
    card_ids = [int(card['id']) for card in response]

    response, status = move_cards(card_ids, "Hungarian", "User 1")
    print(response, status, '\n\n')
#
#    response = reschedule_card(response['card_id'], "2024-01-01")
#    print(response, '\n\n')
#
#    response = reschedule_cards_by_tag("geography", "2024-01-01")
#    print(response, '\n\n')
#
#    response = reschedule_cards_by_deck(1, "2024-01-01")
#    print(response, '\n\n')
#
#    response = reposition_card(response['card_id'], 1)
#    print(response, '\n\n')
#
#    response = reposition_cards_by_tag("geography", 1)
#    print(response, '\n\n')
#
#    response = reposition_cards_by_deck(1, 1)
#    print(response, '\n\n')
#
#    response = reset_card(response['card_id'])
#    print(response, '\n\n')
#
#    response = reset_cards_by_tag("geography")
#    print(response, '\n\n')
#
#    response = reset_cards_by_deck(1)
#    print(response, '\n\n')
#
#    response = suspend_card(response['card_id'])
#    print(response, '\n\n')
#
#    response = suspend_cards_by_tag("geography")
#    print(response, '\n\n')
#
#    response = suspend_cards_by_deck(1)
#    print(response, '\n\n')
#
#    response = bury_card(response['card_id'])
#    print(response, '\n\n')
#
#    response = bury_cards_by_tag("geography")
#    print(response, '\n\n')
#
#    response = bury_cards_by_deck(1)
#    print(response, '\n\n')
#
#    response = get_card_contents(response['card_id'])
#    print(response, '\n\n')
#
#    response = get_card_by_id(response['card_id'])
#    print(response, '\n\n')
#
#    response = get_cards_by_tag("geography")
#    print(response, '\n\n')
#
#    response = get_cards_by_state(1, "due")
#    print(response, '\n\n')
#
#    response = get_cards_by_tag_and_state("geography", "due")
#    print(response, '\n\n')
#
#    response = delete_card(response['card_id'])
#    print(response, '\n\n')
#
#    response = delete_cards_by_tag("geography")
#    print(response, '\n\n')
#
#    response = delete_cards_by_deck(1)
#    print(response, '\n\n')
#