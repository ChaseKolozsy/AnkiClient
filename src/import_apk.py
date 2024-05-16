import requests
from pathlib import Path

# Specify the URL of the API endpoint
url = 'http://localhost:5001/api/import-package'

# Username to be passed as a query parameter
username = 'User 1'  # Replace 'your_username' with the actual username

# Append the username to the URL as a query parameter
url_with_username = f"{url}?username={username}"

# Path to the Anki package file
home_dir = Path.home()
anki_package_path = home_dir / 'Documents/FromX2Ank/AnkiClient/apkgs/0_Video_Segments.apkg'

# Prepare the file to be uploaded
with open(anki_package_path, 'rb') as file:
    files = {'file': file}

    # Make the POST request to upload the Anki package file
    response = requests.post(url_with_username, files=files)

    # Check if the response is valid and is JSON
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

