import requests

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


def sync_user_login(profile_name, username, password, endpoint=None):
    url = f"{BASE_URL}/sync-login"
    data = {"profile_name": profile_name, "username": username, "password": password, "endpoint": endpoint}
    
    try:
        response = requests.post(url, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    from dotenv import dotenv_values
    from deck_ops import get_decks

    env_vars = dotenv_values()
    profile_name = "User 1"

    # Test creating a user
    print(create_user(profile_name))

    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = env_vars['ANKI_ENDPOINT']
    print(sync_user_login(profile_name, username, password, endpoint))

    print(get_decks(profile_name))

    # Test deleting a user
    input = input(f"ready to delete user '{profile_name}'? y/n: ") 
    if input == 'y':
        print(delete_user(profile_name))

