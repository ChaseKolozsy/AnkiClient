import requests
from dotenv import dotenv_values
from pathlib import Path


BASE_URL = "http://localhost:5001/api/db"


def sync_db(username, hkey, endpoint, sync_media=False, upload=False):
    response = requests.post(f"{BASE_URL}/sync", json={
        'username': username, 
        'hkey': hkey, 
        'endpoint': endpoint, 
        'sync_media': sync_media,
        'upload': upload
    })
    print(response)
    try:
        return response.json()
    except:
        return response.text


def sync_status(username, hkey, endpoint):
    response = requests.post(f"{BASE_URL}/sync_status", json={'username': username, 'hkey': hkey, 'endpoint': endpoint})
    return response.json()

def media_sync_status(username):
    response = requests.post(f"{BASE_URL}/media_sync_status", json={'username': username})
    return response.json()



def test_db_ops():
    from note_ops import get_notetypes
    from user_ops import create_user, delete_user, sync_user_login
    from deck_ops import create_deck, get_decks
    from import_ops import upload_anki_package, post_zip_file_to_unzip_media, upload_csv_file
    from pathlib import Path
    import time

    ## ----------------------------------- Initialize ------------------------------------- ##
    env_vars = dotenv_values()
    profile_name = "admin"

    # Test creating a user
    print(create_user(profile_name))

    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']
    upload = False

    if "172.17.0.3" in endpoint:
        print(f"endpoint: {endpoint}, username: {username}, password: {password}")
        home = Path.home()
        #file_name = 'directions.zip'
        #zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
        #zip_file_result = post_zip_file_to_unzip_media(zip_file_path, profile_name)
        #print(zip_file_result)

        #deck_name = 'Hungarian'
        #deck_id = create_deck(deck_name, profile_name)['id']
        #notetype = 'Basic' 
        #delimiter = 'TAB'
        #print(deck_id)

        #file_name = 'Directions-recite.txt'
        #file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
        #upload_csv_file(profile_name, file_path, deck_name, notetype, delimiter)

    try:
        response = sync_user_login(profile_name=profile_name, username=username, password=password, endpoint=endpoint, upload=upload)
        print(response)
        hkey = response['hkey']

        time.sleep(10)
        print(get_decks(profile_name))
        
        #anki_package_path = Path.home() / "Documents/FromX2Ank/AnkiClient/data/apkgs/0_Video_Segments.apkg"
        #response = upload_anki_package(profile_name, anki_package_path)
        #print(response)
    except Exception as e:
        print(f"Error: {e}")
    ## ----------------------------------- Test DB ------------------------------------- ##
    try:
        print(sync_db(profile_name, hkey, endpoint, upload=upload))
    except Exception as e:
        print(f"Error: {e}")

    input = input(f"ready to delete user '{profile_name}'? y/n: ") 
    if input == 'y':
        print(delete_user(profile_name))


if __name__ == "__main__":
    import os
    env_vars = dotenv_values()
    username = env_vars['ANKI_USERNAME']
    #username = "tracychasek@gmail.com"
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']
    hkey = env_vars['ANKI_HKEY']
    #hkey = 'f_mu!A<xnJb`i>eK'
    profile_name = 'chase'
    #profile_name = 'sekeda'
    upload = False
    #from user_ops import sync_user_login
    #response = sync_user_login(profile_name=profile_name, username=username, password=password, endpoint=endpoint, upload=upload)
    #print(response)
    #hkey = response['hkey']
    endpoint = endpoint
    print(sync_db(profile_name, hkey, endpoint, upload=upload))
