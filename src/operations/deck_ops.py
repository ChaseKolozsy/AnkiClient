import requests
from note_ops import get_notetypes
import json

BASE_URL = "http://localhost:5001/api/decks"

def create_deck(deck_name):
    response = requests.post(f"{BASE_URL}/create/{deck_name}")
    return response.json()

def create_filtered_deck(deck_name, search_query, limit, delays):
    data = {
        "deck_name": deck_name,
        "search_query": search_query,
        "limit": limit,
        "delays": delays
    }
    response = requests.post(f"{BASE_URL}/create-filtered", json=data)
    return response.json()

def change_deck_notetype(deck_id, new_notetype_id):
    data = {"new_notetype_id": new_notetype_id}
    response = requests.post(f"{BASE_URL}/{deck_id}/change-notetype", json=data)
    return response.json()

def set_new_card_limit(deck_id, new_card_limit):
    data = {"new_card_limit": new_card_limit}
    response = requests.post(f"{BASE_URL}/{deck_id}/set-new-card-limit", json=data)
    return response.json()

def set_current_deck(deck_id):
    response = requests.post(f"{BASE_URL}/set-current/{deck_id}")
    return response.json()

def create_config(name, new_cards_per_day, review_cards_per_day, new_mix, interday_learning_mix, review_order):
    data = {
        "name": name,
        "new_cards_per_day": new_cards_per_day,
        "review_cards_per_day": review_cards_per_day,
        "new_mix": new_mix,
        "interday_learning_mix": interday_learning_mix,
        "review_order": review_order
    }
    response = requests.post(f"{BASE_URL}/config/create", json=data)
    return response.json()

def apply_config(deck_id, config_id):
    data = {"config_id": config_id}
    response = requests.post(f"{BASE_URL}/{deck_id}/config/apply", json=data)
    return response.json()

def update_deck_mix(deck_id, new_mix, interday_learning_mix, review_order):
    data = {
        "new_mix": new_mix,
        "interday_learning_mix": interday_learning_mix,
        "review_order": review_order
    }
    response = requests.post(f"{BASE_URL}/{deck_id}/update_mix", json=data)
    return response.json()

def delete_deck(deck_id):
    response = requests.delete(f"{BASE_URL}/delete/{deck_id}")
    return response.json()

def delete_filtered_deck(deck_id):
    response = requests.delete(f"{BASE_URL}/delete-filtered/{deck_id}")
    return response.json()

def rename_deck(deck_id, new_name):
    response = requests.put(f"{BASE_URL}/rename/{deck_id}/{new_name}")
    return response.json()

def get_decks():
    response = requests.get(f"{BASE_URL}")
    return response.json()

def get_deck(deck_id):
    response = requests.get(f"{BASE_URL}/{deck_id}")
    return response.json()

def get_cards_in_deck(deck_id):
    response = requests.get(f"{BASE_URL}/{deck_id}/cards")
    return response.json()

def get_current_deck_id():
    response = requests.get(f"{BASE_URL}/get-current-id")
    return response.json()

def get_current_deck():
    response = requests.get(f"{BASE_URL}/current")
    return response.json()

def get_active_decks():
    response = requests.get(f"{BASE_URL}/active")
    return response.json()

def get_deck_config(deck_id):
    response = requests.get(f"{BASE_URL}/{deck_id}/config")
    return response.json()

def get_deck_config_enums():
    response = requests.get(f"{BASE_URL}/config/enums")
    return response.json()

if __name__ == "__main__":
    notetypes = get_notetypes()
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']

    # Assuming the 'Basic' notetype ID is 1 (as per your instruction)
    basic_notetype_id = notetype_dict['Basic']
    # Create a deck
    create_deck_response = create_deck("New Deck")
    print(create_deck_response)
    deck_id = create_deck_response['id']
    print(f"deck_id: {deck_id}")

    ## Change deck notetype
    change_deck_notetype_response = change_deck_notetype(deck_id, basic_notetype_id)
    print(change_deck_notetype_response)

    ## Set new card limit
    set_new_card_limit_response = set_new_card_limit(deck_id, 50)
    print(set_new_card_limit_response)

    ## Set current deck
    set_current_deck_response = set_current_deck(deck_id)
    print(set_current_deck_response)

    ## Create a configuration
    get_deck_config_response = get_deck_config(deck_id)
    print('\n\n-------\n\n', get_deck_config_response, '\n\n------\n\n')
    deck_config = get_deck_config_response['config']
    deck_config_enums = get_deck_config_enums()
    for key, value in deck_config_enums.items():
        print("\n", key, ":\n")
        for enum_key, enum_value in value.items():
            print(f"{enum_key}: {enum_value}")

    # Accessing the enums from the dictionary
    new_mix = deck_config_enums['ReviewMix']['REVIEW_MIX_AFTER_REVIEWS']
    interday_learning_mix = deck_config_enums['ReviewMix']['REVIEW_MIX_MIX_WITH_REVIEWS']
    review_order = deck_config_enums['ReviewCardOrder']['REVIEW_CARD_ORDER_RANDOM']

    print(f"new_mix: {new_mix}, interday_learning_mix: {interday_learning_mix}, review_order: {review_order}")

    create_config_response = create_config(
        "Custom Config",
        new_cards_per_day=20,
        review_cards_per_day=100,
        new_mix=new_mix,
        interday_learning_mix=interday_learning_mix,
        review_order=review_order
    )
    print(create_config_response)

    # Apply a configuration (assuming config_id is 2)
    apply_config_response = apply_config(deck_id, 2)
    print(apply_config_response)

    # Update deck mix
    update_deck_mix_response = update_deck_mix(
        1,
        new_mix=new_mix,
        interday_learning_mix=interday_learning_mix,
        review_order=review_order
    )
    print(update_deck_mix_response)

    # Rename a deck
    rename_deck_response = rename_deck(deck_id, "Renamed Deck")
    print(rename_deck_response)
    print('\n\n-------------------\n\n')

    ## Get all decks
    get_decks_response = get_decks()
    print(get_decks_response)

    print('\n\n-------------------\n\n')

    ## Get a specific deck
    get_deck_response = get_deck(deck_id)
    print(get_deck_response)

    print('\n\n-------------------\n\n')

    ## Get cards in a deck
    get_cards_in_deck_response = get_cards_in_deck(deck_id)
    print(get_cards_in_deck_response)

    print('\n\n-------------------\n\n')

    ## Get current deck ID
    get_current_deck_id_response = get_current_deck_id()
    print(get_current_deck_id_response)

    print('\n\n-------------------\n\n')

    ## Get current deck
    get_current_deck_response = get_current_deck()
    print(get_current_deck_response)

    print('\n\n-------------------\n\n')

    ## Get active decks
    get_active_decks_response = get_active_decks()
    print(get_active_decks_response)


    print('\n\n-------------------\n\n')

    # Delete a deck
    delete_deck_response = delete_deck(1)
    print(delete_deck_response)


    print('\n\n-------------------\n\n')


    ### Delete a filtered deck
    delete_filtered_deck_response = delete_filtered_deck(deck_id)
    print(delete_filtered_deck_response)