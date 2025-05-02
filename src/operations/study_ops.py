import requests
import base64
import os

BASE_URL = 'http://localhost:5001/api'
media_path = './data/media/tmp'

def study(*, deck_id: int, action: str, username: str, base_url: str = BASE_URL) -> tuple[dict, int]:
    url = f"{base_url}/study"
    response = requests.post(url, json={"action": action, "deck_id": deck_id, "username": username})
    response_data = response.json()

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

def study_custom_session(*, username: str, original_deck_id: int, custom_study_params: dict, base_url: str = BASE_URL) -> None:
    """
    Creates a custom study session and then immediately starts studying it.
    
    Args:
        username: The username of the profile
        original_deck_id: The ID of the original deck
        custom_study_params: Parameters for creating the custom study session
        base_url: The base URL for the API
    
    Returns:
        None - this function manages the interactive study session
    """
    # First create the custom study session
    response_data, status_code = create_custom_study_session(
        username=username, 
        deck_id=original_deck_id, 
        custom_study_params=custom_study_params
    )
    
    if status_code != 200:
        print(f"Error creating custom study session: {response_data}")
        return
    
    # Extract the created deck ID
    created_deck_id = response_data.get('created_deck_id')
    
    if not created_deck_id:
        print("No deck ID returned for custom study session. Looking up Custom Study Session deck...")
        
        # Try to find the Custom Study Session deck
        import deck_ops
        decks = deck_ops.get_decks(username)
        for deck in decks:
            if deck['name'] == "Custom Study Session":
                created_deck_id = deck['id']
                print(f"Found Custom Study Session deck with ID: {created_deck_id}")
                break
        
        if not created_deck_id:
            print("Could not find Custom Study Session deck. Using original deck ID.")
            created_deck_id = original_deck_id
    else:
        print(f"Custom study session created with deck ID: {created_deck_id}")
    
    # Now start a study session with this deck
    review_session(created_deck_id, username)

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

def test_study_ops():
    from pathlib import Path
    import user_ops
    import deck_ops
    import import_ops
    import db_ops
    import time
    from dotenv import dotenv_values

    env_vars = dotenv_values()
    profile_name = "chase"
    # Test creating a user
    #print(user_ops.create_user(profile_name))

    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']
    result = user_ops.sync_user_login(profile_name=profile_name, username=username, password=password, endpoint=endpoint, upload=True, sync_media=False)
    print(result)
    hkey = result['hkey']

   # home = Path.home()

   # username = "testuser"
   # response = user_ops.create_user(username)
   # print(response)
   # deck_id = deck_ops.create_deck(deck_name="testdeck", username=username)['id']
   # print(deck_id)

   # file_name = '0_Video_Segments.apkg'
   # file_path = home / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
   # import_ops.upload_anki_package(username, file_path)

   # file_name = 'test.apkg'
   # file_path = home / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
   # import_ops.upload_anki_package(username, file_path)

   # notetype = 'Basic' 
   # deck_name = 'testdeck'
   # delimiter = 'TAB'

   # file_name = 'food.zip'
   # zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
   # zip_file_result = import_ops.post_zip_file_to_unzip_media(zip_file_path, username)
   # print(zip_file_result)

   # file_name = 'Food-recite.txt'
   # file_path = home / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
   # import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

   # file_name = 'directions.zip'
   # zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
   # zip_file_result = import_ops.post_zip_file_to_unzip_media(zip_file_path, username)
   # print(zip_file_result)

   # file_name = 'Directions-recite.txt'
   # file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
   # import_ops.upload_csv_file(username, file_path, deck_name, notetype, delimiter)

   # review_session(deck_id, username)

   # custom_study_params = {
   #     "new_limit_delta": 20,
   #     "cram": {
   #         "kind": "CRAM_KIND_NEW",
   #         "card_limit": 20,
   #         "tags_to_include": ["Food"],
   #         "tags_to_exclude": []
   #     }
   # }

   # try:
   #     response, status_code = create_custom_study_session(username=username, deck_id=deck_id, custom_study_params=custom_study_params)
   # except Exception as e:
   #     user_ops.delete_user(username)
   #     raise e
   # print(f"Status Code: {status_code}")
   # print(f"Response: {response}")

    response = deck_ops.get_decks(profile_name)
    print(response)
    deck_dict = {}
    for deck in response:
        deck_dict[deck['name']] = deck['id']
        print(deck_dict)

    review_session(deck_dict['HungarianGrammarPoints'], profile_name)


    #review_session(deck_dict['0: Video Segments'], profile_name)
    #review_session(deck_dict['Test'], username)

    #input = input("ready to delete user? y/n: ") 
    #if input == 'y':
    #    print(user_ops.delete_user(username))
    #    media_files = os.listdir(media_path)
    #    for file in media_files:
    #        file_path = os.path.join(media_path, file)
    #        if os.path.isfile(file_path):
    #            os.remove(file_path)



if __name__ == "__main__":
    # Setup parameters for custom study
    custom_study_params = {
        "new_limit_delta": 0,
        "cram": {
            "kind": "CRAM_KIND_DUE",  # Study due cards
            "card_limit": 1000,        # Limit to 1000 cards max
            "tags_to_include": [],     # No tag filtering
            "tags_to_exclude": []      # No tag exclusions
        }
    }
    username = "chase"
    deck_id = 1745682159947
    
    # Option 1: Create custom study session and show results
    print("Creating custom study session...")
    custom_study_session, status_code = create_custom_study_session(
        username=username, 
        deck_id=deck_id, 
        custom_study_params=custom_study_params
    )
    import json
    print(f"Status code: {status_code}")
    print(json.dumps(custom_study_session, indent=4, ensure_ascii=False))
    _ = study(deck_id=custom_study_session['created_deck_id'], action='start', username=username)
    print(json.dumps(_, indent=4, ensure_ascii=False))

