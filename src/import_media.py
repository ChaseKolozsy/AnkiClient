import requests
from pathlib import Path

def post_zip_file_to_unzip_media(zip_file_path, username):
    url = "http://localhost:5001/api/unzip-media?username=" + username

    files = {'file': open(zip_file_path, 'rb')}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        print("Media files unzipped successfully")
    else:
        print("Error:", response.json()['error'])

# Example usage
if __name__ == "__main__":
    home = Path.home()
    file_name = input("Enter the name of the zip file: ")
    zip_file_path = home / f'Documents/FromX2Ank/AnkiClient/media/{file_name}'
    username = "User_1"
    post_zip_file_to_unzip_media(zip_file_path, username)

