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

        ## Answer the current card with ease level 3
        try:
            print(study(deck_id=deck_id, action='3', username=username))
        except Exception as e:
            print(e)

        ## Close the review session
        print(study(deck_id=deck_id, action='close', username=username))

        choice = input("hit 'q' to quit, else, any key to continue: ")

    input = input("ready to delete user? y/n: ") 
    if input == 'y':
        print(user_ops.delete_user(username))

