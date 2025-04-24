import requests

BASE_URL = "http://localhost:5001"

# Specify the URL of the API endpoint
def upload_anki_package(username, file_path):
    url = f'{BASE_URL}/api/import-package'
    url_with_username = f"{url}?username={username}"

    with open(file_path, 'rb') as file:
        files = {'file': file}

        response = requests.post(url_with_username, files=files)

        if response.status_code == 200:
            try:
                print(response.json())
            except ValueError:
                print("Response is not in JSON format.")
        else:
            try:
                print(response.json())
            except ValueError:
                print("bad response")
                pass
            print(f"Failed to upload package. Status code: {response.status_code}")

def upload_csv_file(username, file_path, target_deck, notetype, delimiter):
    url = f'{BASE_URL}/api/import-csv'
    url_with_arguments = f"{url}?username={username}&target_deck={target_deck}&notetype={notetype}&delimiter={delimiter}"
    print(url_with_arguments)
    print(f'{file_path}, {target_deck}, {notetype}, {delimiter}')

    with open(file_path, 'rb') as file:
        files = {'file': file}

        response = requests.post(url_with_arguments, files=files)

        if response.status_code == 200:
            try:
                print(response.json())
            except ValueError:
                print("Response is not in JSON format.")
        else:
            try:
                print(f'Error: {response.json()}')
            except ValueError:
                print("Bad response")
                pass
            print(f"Failed to upload CSV file. Status code: {response.status_code}")

def post_zip_file_to_unzip_media(zip_file_path, username):
    url = f'{BASE_URL}/api/unzip-media?username={username}'

    files = {'file': open(zip_file_path, 'rb')}
    try:
        response = requests.post(url, files=files)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def upload_media_file(username, media_file_path):
    url = f'{BASE_URL}/api/import-media?username={username}'
    files = {'file': open(media_file_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()

def test_import_ops():
    from user_ops import delete_user, create_user
    from deck_ops import create_deck
    from pathlib import Path

    username = "User 1"
    print(create_user(username))

    home = Path.home()
    file_name = 'directions.zip'
    zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{file_name}'
    zip_file_result = post_zip_file_to_unzip_media(zip_file_path, username)
    print(zip_file_result)

    media_file = 'A büfében.mp3'

    media_file_path = home / f'Documents/FromX2Ank/AnkiClient/data/media/{media_file}'

    upload_media_result = upload_media_file(username, media_file_path)
    print(upload_media_result)

    #choice = input("apgk: 1 or csv: 2, ")

    #if choice == "1":
    #    file_name = input("Enter the name of the Anki package file: ")
    #    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/apkgs/{file_name}'
    #    upload_anki_package(username, file_path)

    #if choice == "2":
    #    file_name = input("Enter the name of the CSV file: ")
    #    deck_name = input("Enter the deck name: ")
    #    notetype = input("Enter the notetype: ")
    #    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/csv_files/{file_name}'
    #    delimiter = input("Enter the delimiter: ")
    #    upload_csv_file(username, file_path, deck_name, notetype, delimiter)


    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    deck_name = 'Hungarian'
    deck_id = create_deck(deck_name, username)['id']
    notetype = 'Basic' 
    delimiter = 'TAB'
    print(deck_id)

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    print(delete_user(username))

if __name__ == "__main__":
    from pathlib import Path
    username = "User 1"
    file_name = 'Hungarian_grammar_points.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/aXaTT/submodules/anki/client/data/exports/{username}/{file_name}'
    print(upload_anki_package(username, file_path))
