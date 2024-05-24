import requests
import user_ops
import deck_ops
import import_ops
from pathlib import Path

BASE_URL = 'http://localhost:5001/api'

def study(*, deck_id: int, action: str, username: str, base_url: str = BASE_URL) -> tuple[dict, int]:
    url = f"{base_url}/study"
    response = requests.post(url, json={"action": action, "deck_id": deck_id, "username": username})
    
    return response.json(), response.status_code

def create_custom_study_session(*, username: str, deck_id: int, custom_study_params: dict, base_url: str = BASE_URL) -> tuple[dict, int]:
    url = f"{base_url}/custom_study"
    payload = {
        "username": username,
        "deck_id": deck_id,
        "custom_study_params": custom_study_params
    }
    response = requests.post(url, json=payload)
    return response.json(), response.status_code



def review_session(deck_id: int, username: str):
    choice = ""
    while choice != 'q':
        # Start a review session
        try:
            print(study(deck_id=deck_id, action='start', username=username))
        except Exception as e:
            print(e)

        # Flip the current card
        try:
            print(study(deck_id=deck_id, action='flip', username=username))
        except Exception as e:
            print(e)

        # Answer the current card with ease level 3
        try:
            print(study(deck_id=deck_id, action='3', username=username))
        except Exception as e:
            print(e)

        # Close the review session
        print(study(deck_id=deck_id, action='close', username=username))

        choice = input("hit 'q' to quit, else, any key to continue: ")

if __name__ == "__main__":
    username = "testuser"
    response = user_ops.create_user(username)
    print(response)
    deck_id = deck_ops.create_deck(deck_name="testdeck", username=username)['id']
    print(deck_id)

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    import_ops.upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'testdeck'
    delimiter = 'TAB'

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    review_session(deck_id, username)


    #custom_study_params = {
    #    "new_limit_delta": 10,
    #    "review_limit_delta": 20,
    #    "forgot_days": 0,
    #    "review_ahead_days": 5,
    #    "preview_days": 3,
    #    "cram": {
    #        "kind": "CRAM_KIND_DUE",
    #        "card_limit": 20,
    #        "tags_to_include": ["Food"],
    #        "tags_to_exclude": []
    #    }
    #}

    custom_study_params = {
        "new_limit_delta": 20,
        "cram": {
            "kind": "CRAM_KIND_NEW",
            "card_limit": 20,
            "tags_to_include": ["Food"],
            "tags_to_exclude": []
        }
    }

    try:
        response, status_code = create_custom_study_session(username=username, deck_id=deck_id, custom_study_params=custom_study_params)
    except Exception as e:
        user_ops.delete_user(username)
        raise e
    print(f"Status Code: {status_code}")
    print(f"Response: {response}")

    response = deck_ops.get_decks(username)
    print(response)
    deck_dict = {}
    for deck in response:
        deck_dict[deck['name']] = deck['id']

    print(deck_dict)

    review_session(deck_dict['Custom Study Session'], username)

    input = input("ready to delete user? y/n: ") 
    if input == 'y':
        print(user_ops.delete_user(username))

