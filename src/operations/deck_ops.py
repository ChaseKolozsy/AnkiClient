import requests

BASE_URL = "http://localhost:5001/api/decks"

def create_deck(deck_name, username):
    url = f"{BASE_URL}/create/{deck_name}"
    data = {"username": username}
    response = requests.post(url, json=data)
    return response.json()

def change_deck_notetype(deck_id, new_notetype_id, username, match_by_name=True):
    url = f"{BASE_URL}/{deck_id}/change-notetype"
    data = {
        "new_notetype_id": new_notetype_id,
        "match_by_name": match_by_name,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def set_new_card_limit(deck_id, new_card_limit, username):
    url = f"{BASE_URL}/{deck_id}/set-new-card-limit"
    data = {
        "new_card_limit": new_card_limit,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def set_current_deck(deck_id, username):
    url = f"{BASE_URL}/set-current/{deck_id}"
    data = {"username": username}
    response = requests.post(url, json=data)
    return response.json()

def create_config(*, 
                  name: str, 
                  new_cards_per_day: int, 
                  review_cards_per_day: int, 
                  new_mix: int, 
                  interday_learning_mix: int, 
                  review_order: int, 
                  username: str) -> dict:
    url = f"{BASE_URL}/config/create"
    data = {
        "name": name,
        "new_cards_per_day": new_cards_per_day,
        "review_cards_per_day": review_cards_per_day,
        "new_mix": new_mix,
        "interday_learning_mix": interday_learning_mix,
        "review_order": review_order,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def apply_config(deck_id, config_id, username):
    url = f"{BASE_URL}/{deck_id}/config/apply"
    data = {
        "config_id": config_id,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def update_deck_mix(deck_id, new_mix, interday_learning_mix, review_order, username):
    url = f"{BASE_URL}/{deck_id}/update_mix"
    data = {
        "new_mix": new_mix,
        "interday_learning_mix": interday_learning_mix,
        "review_order": review_order,
        "username": username
    }
    response = requests.post(url, json=data)
    return response.json()

def delete_deck(deck_id, username):
    url = f"{BASE_URL}/delete/{deck_id}"
    data = {"username": username}
    response = requests.delete(url, json=data)
    return response.json()

def delete_filtered_deck(deck_id, username):
    url = f"{BASE_URL}/delete-filtered/{deck_id}"
    data = {"username": username}
    response = requests.delete(url, json=data)
    return response.json()

def rename_deck(deck_id, new_name, username):
    url = f"{BASE_URL}/rename/{deck_id}/{new_name}"
    data = {"username": username}
    response = requests.put(url, json=data)
    return response.json()

def get_decks(username):
    url = BASE_URL
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_deck(deck_id, username):
    url = f"{BASE_URL}/{deck_id}"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_cards_in_deck(deck_id, username):
    url = f"{BASE_URL}/{deck_id}/cards"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_current_deck_id(username):
    url = f"{BASE_URL}/get-current-id"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_current_deck(username):
    url = f"{BASE_URL}/current"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_active_decks(username):
    url = f"{BASE_URL}/active"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()

def get_deck_config_enums():
    url = f"{BASE_URL}/config/enums"
    url = f"{BASE_URL}/config/enums"
    response = requests.get(url)
    return response.json()

def get_deck_config(deck_id, username):
    url = f"{BASE_URL}/{deck_id}/config"
    data = {"username": username}
    response = requests.get(url, json=data)
    return response.json()


#if __name__ == "__main__":
#    from note_ops import get_notetypes
#    from user_ops import create_user, delete_user
#    from deck_ops import create_deck
#    from import_ops import upload_anki_package, upload_csv_file
#    from pathlib import Path
#
#    ## ----------------------------------- Initialize ------------------------------------- ##
#    username = "test_user"  # Replace with the actual username
#    print(create_user(username))
#    deck_id = create_deck(deck_name="testdeck", username=username)['id']
#    print(deck_id)
#
#    file_name = '0_Video_Segments.apkg'
#    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
#    upload_anki_package(username, file_path)
#
#    notetype = 'Basic' 
#    deck_name = 'testdeck'
#    delimiter = 'TAB'
#
#    file_name = 'Food-recite.txt'
#    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
#    upload_csv_file(username, file_path, deck_name, notetype, delimiter)
#
#    file_name = 'Directions-recite.txt'
#    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
#    upload_csv_file(username, file_path, deck_name, notetype, delimiter)
#
#    # Assuming get_notetypes is defined elsewhere and returns a list of notetypes
#    notetypes = get_notetypes(username)
#    notetype_dict = {}
#    if notetypes:
#        print("Notetypes retrieved successfully:")
#        for notetype in notetypes:
#            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
#            notetype_dict[notetype['name']] = notetype['id']
#
#    # Assuming the 'Basic' notetype ID is 1 (as per your instruction)
#    basic_notetype_id = notetype_dict['Basic']
#
#
#    ## ----------------------------------- Test Decks ------------------------------------- ##
#
#    # Create a deck
#    create_deck_response = create_deck("New Deck", username)
#    print(create_deck_response)
#    old_deck_id = deck_id
#    deck_id = create_deck_response['id']
#    print(f"deck_id: {deck_id}")
#
#    # Change deck notetype
#    change_deck_notetype_response = change_deck_notetype(deck_id, basic_notetype_id, username)
#    print(change_deck_notetype_response)
#
#    # Set new card limit
#    set_new_card_limit_response = set_new_card_limit(deck_id, 50, username)
#    print(set_new_card_limit_response)
#
#    # Set current deck
#    set_current_deck_response = set_current_deck(deck_id, username)
#    print(set_current_deck_response)
#
#    # Create a configuration
#    get_deck_config_response = get_deck_config(deck_id, username)
#    print('\n\n-------\n\n', get_deck_config_response, '\n\n------\n\n')
#    deck_config = get_deck_config_response['config']
#    deck_config_enums = get_deck_config_enums()
#    for key, value in deck_config_enums.items():
#        print("\n", key, ":\n")
#        for enum_key, enum_value in value.items():
#            print(f"{enum_key}: {enum_value}")
#
#    # Accessing the enums from the dictionary
#    new_mix = deck_config_enums['ReviewMix']['REVIEW_MIX_AFTER_REVIEWS']
#    interday_learning_mix = deck_config_enums['ReviewMix']['REVIEW_MIX_MIX_WITH_REVIEWS']
#    review_order = deck_config_enums['ReviewCardOrder']['REVIEW_CARD_ORDER_RANDOM']
#
#    print(f"new_mix: {new_mix}, interday_learning_mix: {interday_learning_mix}, review_order: {review_order}")
#
#    create_config_response = create_config(
#        name="Custom Config",
#        new_cards_per_day=20,
#        review_cards_per_day=100,
#        new_mix=new_mix,
#        interday_learning_mix=interday_learning_mix,
#        review_order=review_order,
#        username=username
#    )
#    print(create_config_response)
#
#    # Apply a configuration (assuming config_id is 2)
#    apply_config_response = apply_config(deck_id, 2, username)
#    print(apply_config_response)
#
#    # Update deck mix
#    update_deck_mix_response = update_deck_mix(
#        deck_id,
#        new_mix=new_mix,
#        interday_learning_mix=interday_learning_mix,
#        review_order=review_order,
#        username=username
#    )
#    print(update_deck_mix_response)
#
#    # Rename a deck
#    print('\n\n------ Rename a deck -------------\n\n')
#    rename_deck_response = rename_deck(deck_id, "Renamed Deck", username)
#    print(rename_deck_response)
#    print('\n\n-------------------\n\n')
#
#    # Get all decks
#    print('\n\n------ Get all decks -------------\n\n')
#    get_decks_response = get_decks(username)
#    print(get_decks_response)
#
#    print('\n\n------ Get deck by id -------------\n\n')
#
#    # Get a specific deck
#    get_deck_response = get_deck(deck_id, username)
#    print(get_deck_response)
#
#    print('\n\n------ Get cards in a deck -------------\n\n')
#
#    # Get cards in a deck
#    get_cards_in_deck_response = get_cards_in_deck(old_deck_id, username)
#    print(get_cards_in_deck_response)
#
#    print('\n\n------ Get current deck id -------------\n\n')
#
#    # Get current deck ID
#    get_current_deck_id_response = get_current_deck_id(username)
#    print(get_current_deck_id_response)
#
#    print('\n\n------ Get current deck -------------\n\n')
#
#    # Get current deck
#    get_current_deck_response = get_current_deck(username)
#    print(get_current_deck_response)
#
#    print('\n\n------ Get active decks -------------\n\n')
#
#    # Get active decks
#    get_active_decks_response = get_active_decks(username)
#    print(get_active_decks_response)
#
#    print('\n\n------ Delete a deck -------------\n\n')
#
#    # Delete a deck
#    delete_deck_response = delete_deck(deck_id, username)
#    print(delete_deck_response)
#
#
#    delete_user(username)

if __name__ == "__main__":
    import json
    user_1 = "User 1"
    user_2 = 'chase'
    decks_1 = get_decks(user_1)
    decks_2 = get_decks(user_2)
    deck_id_1 = 1747127569453
    deck_id_2 = 1745682159947
    cards_1 = get_cards_in_deck(deck_id_1, user_1)
    cards_2 = get_cards_in_deck(deck_id_2, user_2)
    print(len(cards_1))
    print(len(cards_2))
    print(json.dumps(cards_1[0], indent=4, ensure_ascii=False))
    print(json.dumps(cards_2[0], indent=4, ensure_ascii=False))
    from submodules.anki.client.src.operations.card_ops import get_card_contents
    from submodules.anki.client.src.operations.note_ops import update_note_fields

    for card_x in cards_1:
        card_contents_x = get_card_contents(card_id=card_x['id'], username=user_1)
        fields_x = card_contents_x['fields']
        scenarios = fields_x.pop('scenarios')
        example_x = fields_x.pop('example')
        formula_x = fields_x.pop('formula')
        native_x = fields_x.pop('native_language_explanation')
        target_x = fields_x.pop('target_language_explanation')
        print(json.dumps(scenarios, indent=4, ensure_ascii=False))
        for card_y in cards_2:
            card_contents_y = get_card_contents(card_id=card_y['id'], username=user_2)
            fields_y = card_contents_y['fields']
            example_y = fields_y.pop('example')
            formula_y = fields_y.pop('formula')
            native_y = fields_y.pop('native_language_explanation')
            target_y = fields_y.pop('target_language_explanation')
            if example_x == example_y and formula_x == formula_y and native_x == native_y and target_x == target_y:
                print("\n\n\n------------------ ------ JACKPOT ------ ------------------\n\n\n")
                note_id_y = card_contents_y['note_id']
                fields_x['scenarios'] = scenarios
                result = update_note_fields(note_id=note_id_y, fields=fields_x, username=user_2)
                print(result)

