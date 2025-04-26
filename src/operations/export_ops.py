import requests

BASE_URL = 'http://localhost:5001/api'

def get_exported_collection_package(username, export_path, include_media=False, legacy=False):
    url = f"{BASE_URL}/export-collection-package"
    payload = {
        'include_media': include_media,
        'legacy': legacy
    }
    response = requests.post(url, json=payload, params={'username': username}, stream=True)
    
    if response.status_code == 200:
        with open(export_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"success": True, "message": f"File saved to {export_path}"}
    else:
        return response.json()

def get_exported_anki_package(username, out_path, deck_id, export_path):
    url = f"{BASE_URL}/export-anki-package?username={username}&out_path={out_path}&deck_id={deck_id}"
    response = requests.post(url, stream=True)

    if response.status_code == 200:
        with open(export_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"success": True, "message": f"File saved to {export_path}"}
    else:
        return response.json()

def get_exported_notes_csv(*, 
                           username: str, 
                           out_path: str, 
                           deck_id: int, 
                           export_path: str, 
                           with_html: bool
                           ) -> dict:
    url = f"{BASE_URL}/export-note-csv?username={username}&out_path={out_path}&deck_id={deck_id}&with_html={with_html}"
    response = requests.post(url, stream=True)

    if response.status_code == 200:
        with open(export_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"success": True, "message": f"File saved to {export_path}"}
    else:
        return response.json()

def test_export_ops():
    from user_ops import create_user, delete_user
    from import_ops import upload_anki_package, upload_csv_file
    from pathlib import Path

    username = 'test_user'
    print(create_user(username))

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'Default'
    delimiter = 'TAB'

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    out_path_package = f"/home/anki/.local/share/Anki2/{username}/test.apkg"

    export_package_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/exports/{username}/test.apkg'
    export_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/exports/{username}/collection.apkg'

    export_path.parent.mkdir(parents=True, exist_ok=True)


    result = get_exported_collection_package(username, export_path, include_media=True, legacy=True)
    print(result)

    print(get_exported_anki_package(username, out_path_package, 1, export_package_path))

    out_path_notes = f"/home/anki/.local/share/Anki2/{username}/notes.csv"
    export_csv_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/exports/{username}/notes.csv'
    print(get_exported_notes_csv(username=username, out_path=out_path_notes, deck_id=1, export_path=export_csv_path, with_html=True))

    ready = input("Ready to delete user? (y/n)")
    if ready == 'y':
        delete_user(username)

if __name__ == '__main__':
    from pathlib import Path
    username = "User 1"
    deck_id = "1745664813895"
    out_path_package = f"/home/anki/.local/share/Anki2/{username}/Hungarian_grammar_points.apkg"
    export_path = Path.home() / f'Documents/FromX2Ank/aXaTT/submodules/anki/client/data/exports/{username}/Hungarian_grammar_points.apkg'
    print(get_exported_anki_package(username, out_path_package, deck_id, export_path))