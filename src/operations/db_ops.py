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
    # Load env and ensure endpoint/hkey exist by logging in if missing,
    # then persist them into AnkiClient/.env without overwriting existing values.
    env_vars = dotenv_values()

    profile_name = 'chase'
    username = env_vars['ANKI_USERNAME']
    password = env_vars['ANKI_PASSWORD']
    endpoint = (env_vars.get('ANKI_ENDPOINT') or '').strip()
    hkey = (env_vars.get('ANKI_HKEY') or '').strip()
    upload = False

    missing_endpoint = endpoint == ''
    missing_hkey = hkey == ''

    # Always perform login first to handle FULL_SYNC correctly, and to get fresh hkey/endpoint
    login = None
    try:
        from user_ops import sync_user_login
        # Sanitize endpoint: if it's clearly pointing at our API server or includes '/api', ignore it
        endpoint_arg = endpoint or None
        if endpoint_arg and (
            '/api/' in endpoint_arg or
            'localhost:5001' in endpoint_arg or
            '127.0.0.1:5001' in endpoint_arg or
            endpoint_arg.startswith('http://172.17.')
        ):
            endpoint_arg = None

        login = sync_user_login(
            profile_name=profile_name,
            username=username,
            password=password,
            endpoint=endpoint_arg,
            upload=upload,
            sync_media=False,
        )
        print('login:', login)
        # Update local variables from login response if provided
        if isinstance(login, dict) and 'hkey' in login:
            hkey = login['hkey']
        if isinstance(login, dict) and login.get('endpoint'):
            endpoint = login['endpoint']
    except Exception as e:
        print(f"Login failed while attempting to obtain auth: {e}")

        # Persist values into AnkiClient/.env if we now have them
        try:
            root = Path(__file__).resolve().parents[2]
            env_file = root / '.env'
            lines = []
            if env_file.exists():
                try:
                    lines = env_file.read_text().splitlines()
                except Exception:
                    lines = []

            # Index existing keys -> (idx, value)
            existing = {}
            for idx, line in enumerate(lines):
                if not line or line.lstrip().startswith('#'):
                    continue
                if '=' in line:
                    k, v = line.split('=', 1)
                    existing[k.strip()] = (idx, v)

            def safe_val(v: str) -> str:
                if v is None:
                    return ''
                txt = str(v)
                if any(ch in txt for ch in [' ', '#', '$']):
                    txt = txt.replace("'", "\\'")
                    return f"'{txt}'"
                return txt

            updates = {}
            if hkey and ('ANKI_HKEY' not in existing or not existing['ANKI_HKEY'][1].strip()):
                updates['ANKI_HKEY'] = safe_val(hkey)
            if endpoint and ('ANKI_ENDPOINT' not in existing or not existing['ANKI_ENDPOINT'][1].strip()):
                updates['ANKI_ENDPOINT'] = safe_val(endpoint)

            if updates:
                for k, v in updates.items():
                    if k in existing:
                        idx, _ = existing[k]
                        lines[idx] = f"{k}={v}"
                    else:
                        lines.append(f"{k}={v}")
                content = "\n".join(lines).rstrip('\n') + "\n"
                env_file.write_text(content)
        except Exception as e:
            print(f"Warning: could not update AnkiClient/.env: {e}")

    # If login handled a full sync, skip separate DB sync.
    if isinstance(login, dict) and login.get('full_sync'):
        print("Full sync handled during login:", login)
    else:
        # Proceed with DB sync using the values we have
        # Important: pass None instead of empty string for endpoint
        endpoint_for_sync = endpoint or None
        print(sync_db(profile_name, hkey, endpoint_for_sync, upload=upload))
