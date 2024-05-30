import requests
import base64
import os

BASE_URL = 'http://localhost:5001/api'
media_path = './data/media/tmp'

def study(*, deck_id: int, action: str, username: str, base_url: str = BASE_URL) -> tuple[dict, int]:
    url = f"{base_url}/study"
    response = requests.post(url, json={"action": action, "deck_id": deck_id, "username": username})
    response_data = response.json()

    if 'ease_options' in response_data:
        for ease_option, ease_value in response_data['ease_options'].items():
            print(f"Ease Option: {ease_option}, Ease Value: {ease_value}")
    # Process media files if present
    if 'media_files' in response_data:
        for filename, filedata in response_data['media_files'].items():
            with open(f"{media_path}/{filename}", "wb") as media_file:
                media_file.write(base64.b64decode(filedata))

    return response_data, response.status_code

def create_custom_study_session(*, username: str, deck_id: int, custom_study_params: dict, base_url: str = BASE_URL) -> tuple[dict, int]:
    url = f"{base_url}/custom-study"
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
    from pathlib import Path
    import user_ops
    import deck_ops
    import import_ops

    home = Path.home()

    username = "testuser"
    response = user_ops.create_user(username)
    print(response)
    deck_id = deck_ops.create_deck(deck_name="testdeck", username=username)['id']
    print(deck_id)

    file_name = '0_Video_Segments.apkg'
    file_path = home / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    import_ops.upload_anki_package(username, file_path)

    file_name = 'test.apkg'
    file_path = home / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    import_ops.upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'testdeck'
    delimiter = 'TAB'

    file_name = 'food.zip'
    zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
    zip_file_result = import_ops.post_zip_file_to_unzip_media(zip_file_path, username)
    print(zip_file_result)

    file_name = 'Food-recite.txt'
    file_path = home / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'directions.zip'
    zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
    zip_file_result = import_ops.post_zip_file_to_unzip_media(zip_file_path, username)
    print(zip_file_result)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    review_session(deck_id, username)

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


    review_session(deck_dict['0: Video Segments'], username)
    review_session(deck_dict['Test'], username)

    input = input("ready to delete user? y/n: ") 
    if input == 'y':
        print(user_ops.delete_user(username))
        media_files = os.listdir(media_path)
        for file in media_files:
            file_path = os.path.join(media_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


