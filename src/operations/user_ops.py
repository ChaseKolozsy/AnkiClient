import requests
from pathlib import Path

BASE_URL = "http://localhost:5001/api/users"

def create_user(username):
    url = f"{BASE_URL}/create/{username}"
    response = requests.post(url)
    return response.json()

def delete_user(username):
    url = f"{BASE_URL}/delete/{username}"
    response = requests.delete(url)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Invalid JSON response", "status_code": response.status_code}


def sync_user_login(*, profile_name: str, username: str, password: str, upload: bool = False, endpoint: str = None, sync_media: bool = False):
    url = f"{BASE_URL}/sync-login"
    data = {"profile_name": profile_name, "username": username, "password": password, "endpoint": endpoint, "upload": upload, "sync_media": sync_media}
    
    try:
        response = requests.post(url, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    from dotenv import dotenv_values
    from deck_ops import get_decks
    from import_ops import upload_anki_package
    from db_ops import sync_db
    import time

    env_vars = dotenv_values()
    profile_name = "User 1"

    # Test creating a user
    print(create_user(profile_name))

    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']

    #home = Path.home()
    #file_name = '0_Video_Segments.apkg'
    #file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    #upload_anki_package(profile_name, file_path)

    result = sync_user_login(profile_name=profile_name, username=username, password=password, endpoint=endpoint, upload=True, sync_media=True)
    print(result)
    hkey = result['hkey']
    print(f"hkey: {hkey}")


    # Test deleting a user
    input = input(f"ready to delete user '{profile_name}'? y/n: ") 
    if input == 'y':
        print(delete_user(profile_name))

