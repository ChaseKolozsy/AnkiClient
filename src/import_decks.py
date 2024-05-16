import requests
from pathlib import Path

# Specify the URL of the API endpoint
def upload_anki_package(username, file_path):
    url = 'http://localhost:5001/api/import-package'
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

def upload_csv_file(username, file_path):
    url = 'http://localhost:5001/api/import-csv'
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
                print("Bad response")
                pass
            print(f"Failed to upload CSV file. Status code: {response.status_code}")

if __name__ == "__main__":
    username = "User 1"
    choice = input("apgk: 1 or csv: 2, ")

    if choice == "1":
        file_name = input("Enter the name of the Anki package file: ")
        file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/apkgs/{file_name}'
        upload_anki_package(username, file_path)

    if choice == "2":
        file_name = input("Enter the name of the CSV file: ")
        file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/csv_files/{file_name}'
        upload_csv_file(username, file_path)


