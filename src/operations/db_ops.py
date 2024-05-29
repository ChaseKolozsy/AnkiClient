import requests
from dotenv import dotenv_values
from pathlib import Path


BASE_URL = "http://localhost:5001/api/db"


def sync_db(username, hkey, endpoint):
    response = requests.post(f"{BASE_URL}/sync", json={'username': username, 'hkey': hkey, 'endpoint': endpoint})
    print(response)
    try:
        return response.json()
    except:
        return response.text


if __name__ == "__main__":
    from note_ops import get_notetypes
    from user_ops import create_user, delete_user, sync_user_login
    from deck_ops import create_deck, get_decks
    from import_ops import upload_anki_package
    from pathlib import Path

    ## ----------------------------------- Initialize ------------------------------------- ##
    env_vars = dotenv_values()
    profile_name = "User 1"

    # Test creating a user
    print(create_user(profile_name))

    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']

    response = sync_user_login(profile_name, username, password, endpoint)
    print(response)
    hkey = response['hkey']

    print(get_decks(profile_name))
    
    anki_package_path = Path.home() / "Documents/FromX2Ank/AnkiClient/data/apkgs/0_Video_Segments.apkg"
    response = upload_anki_package(profile_name, anki_package_path)
    print(response)

    ## ----------------------------------- Test DB ------------------------------------- ##
    print(sync_db(profile_name, hkey, endpoint))

    input = input(f"ready to delete user '{profile_name}'? y/n: ") 
    if input == 'y':
        print(delete_user(profile_name))

