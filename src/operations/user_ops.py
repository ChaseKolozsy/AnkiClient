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

if __name__ == "__main__":
    # Test creating a user
    print("Creating user 'testuser':")
    print(create_user('testuser'))

    # Test deleting a user
    print("Deleting user 'testuser':")
    print(delete_user('testuser'))

