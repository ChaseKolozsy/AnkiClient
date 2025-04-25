import requests

BASE_URL = "http://localhost:5001/api/notetypes"

def get_notetypes(username):
    response = requests.get(f"{BASE_URL}/notes", json={"username": username})
    return response.json()

def get_notetype_id_by_card_id(card_id, username):
    response = requests.get(f"{BASE_URL}/cards/{card_id}/notetype", json={"username": username})
    return response.json()

def create_notetype_with_fields(name, fields, base_notetype_id, qfmt, afmt, username):
    data = {
        "name": name,
        "fields": fields,
        "base_notetype_id": base_notetype_id,
        "qfmt": qfmt,
        "afmt": afmt,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/create-with-fields", json=data)
    return response.json()

def set_sort_field(notetype_id, field_name, username):
    data = {
        "field_name": field_name,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/{notetype_id}/set-sort-field", json=data)
    return response.json()

def reorder_fields(notetype_id, new_order, username):
    data = {
        "new_order": new_order,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/{notetype_id}/reorder-fields", json=data)
    return response.json()

def add_template_to_notetype(notetype_id, template_name, qfmt, afmt, username):
    data = {
        "template_name": template_name,
        "qfmt": qfmt,
        "afmt": afmt,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/{notetype_id}/add-template", json=data)
    return response.json()

def update_notetype_css(notetype_id, new_css, username):
    data = {
        "css": new_css,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/{notetype_id}/update-css", json=data)
    return response.json()

def add_field_to_notetype(notetype_id, field_name, username):
    data = {
        "field_name": field_name,
        "username": username
    }
    response = requests.post(f"{BASE_URL}/{notetype_id}/fields", json=data)
    return response.json()

def get_notetype_css(notetype_id, username):
    response = requests.get(f"{BASE_URL}/{notetype_id}/css", json={"username": username})
    return response.json()

def get_notetype_templates(notetype_id, username):
    response = requests.get(f"{BASE_URL}/{notetype_id}/templates", json={"username": username})
    return response.json()

def get_notetype_fields(notetype_id, username):
    response = requests.get(f"{BASE_URL}/{notetype_id}/fields", json={"username": username})
    return response.json()

def get_sort_field(notetype_id, username):
    response = requests.get(f"{BASE_URL}/{notetype_id}/get-sort-field", json={"username": username})
    return response.json()

def remove_field_from_notetype(notetype_id, field_name, username):
    response = requests.delete(f"{BASE_URL}/{notetype_id}/fields/{field_name}", json={"username": username})
    return response.json()

def delete_notetype(notetype_id, username):
    response = requests.delete(f"{BASE_URL}/{notetype_id}/delete", json={"username": username})
    return response.json()

# Example usage

def test_note_ops():
    from user_ops import create_user, delete_user
    from deck_ops import create_deck
    from import_ops import upload_anki_package, upload_csv_file
    from pathlib import Path

    ## ----------------------------------- Initialize ------------------------------------- ##
    username = "test_user"  # Replace with the actual username
    print(create_user(username))
    deck_id = create_deck(deck_name="testdeck", username=username)['id']
    print(deck_id)

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'testdeck'
    delimiter = 'TAB'

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    ## ----------------------------------- Test Notetypes ------------------------------------- ##

    notetypes = get_notetypes(username)
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

    if 'Basic' in notetype_dict:
        notetype_id = notetype_dict['Basic']
        
        print("\nSort Field:")
        sort_field = get_sort_field(notetype_id, username)
        print(sort_field)

        print("\nCSS:")
        css = get_notetype_css(notetype_id, username)
        print(css)

        print("\nTemplates:")
        templates = get_notetype_templates(notetype_id, username)
        print(templates)

        print("\nFields:")
        fields = get_notetype_fields(notetype_id, username)
        print(fields)

    print(add_field_to_notetype(notetype_dict['Basic'], "More Info", username), '\n\n')
    print("changing order: \n")

    notetype_id = notetype_dict['Basic']
    new_order = {
        "Front": 2,
        "Back": 1,
        "More Info": 0  
    }
    result = reorder_fields(notetype_id, new_order, username)

    fields = get_notetype_fields(notetype_dict['Basic'], username)
    print(fields)

    result = set_sort_field(notetype_dict['Basic'], "More Info", username)
    sort_field = get_sort_field(notetype_id, username)
    print(sort_field)

    result = set_sort_field(notetype_dict['Basic'], "Front", username)
    sort_field = get_sort_field(notetype_id, username)
    print(sort_field)
    
    remove_field_from_notetype(notetype_dict['Basic'], "More Info", username)
    print('\n\n')
    notetype_id = notetype_dict['Basic']
    new_order = {
        "Front": 0,
        "Back": 1,
    }
    result = reorder_fields(notetype_id, new_order, username)

    fields = get_notetype_fields(notetype_dict['Basic'], username)
    print(fields)

    print(create_notetype_with_fields("New Notetype", ["Field1", "Field2"], notetype_dict['Basic'], None, None, username), '\n\n')

    notetypes = get_notetypes(username)
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

    for notetype in notetype_dict:
        if 'New Notetype' in notetype:
            result = delete_notetype(notetype_dict[notetype], username)

    notetypes = get_notetypes(username)
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")

    for notetype in notetype_dict:
        if 'New Notetype' in notetype:
            result = delete_notetype(notetype_dict[notetype], username)

    delete_user(username)

if __name__ == "__main__":
    note_types = get_notetypes(username="User 1")
    print(note_types)
    #print(delete_notetype(notetype_id="1745506364405", username="User 1"))