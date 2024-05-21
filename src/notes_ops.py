import requests

def get_notetypes():
    url = "http://localhost:5001/api/notetypes/notes"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_sort_field(notetype_id):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/get-sort-field"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_notetype_css(notetype_id):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/css"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_notetype_templates(notetype_id):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/templates"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_notetype_fields(notetype_id):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/fields"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def add_field_to_notetype(notetype_id, field_name):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/fields"
    data = { "field_name": field_name}
    print(f"Attempting to Add field {field_name} to notetype {notetype_id}")
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(response.json())
        print(f"An error occurred: {e}")
        return None

def delete_field_from_note(notetype_id, field_name):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/fields/{field_name}"

    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an error for bad status codes
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def create_notetype_with_fields(notetype_name, field_names, base_notetype_id):
    url = "http://localhost:5001/api/notetypes/create-with-fields"
    data = {
        "name": notetype_name,
        "fields": field_names,
        "base_notetype_id": base_notetype_id
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if 'response' in locals():
            print(response.json())
        return None

def set_sort_field(notetype_id, field_name):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/set-sort-field"
    data = {"field_name": field_name}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def reorder_notetype_fields(notetype_id, new_order):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/reorder-fields"
    data = {"new_order": new_order}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def delete_notetype_by_id(notetype_id):
    url = f"http://localhost:5001/api/notetypes/{notetype_id}/delete"

    try:
        response = requests.delete(url)
        response.raise_for_status()  # Raise an error for bad status codes

        if response.status_code == 200:
            return "Notetype deleted successfully"
        else:
            return "Failed to delete notetype"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_notetype_id_by_card_id(card_id):
    url = f"http://localhost:5001/api/cards/{card_id}/notetype"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    notetypes = get_notetypes()
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
        sort_field = get_sort_field(notetype_id)
        print(sort_field)

        print("\nCSS:")
        css = get_notetype_css(notetype_id)
        print(css)

        print("\nTemplates:")
        templates = get_notetype_templates(notetype_id)
        print(templates)

        print("\nFields:")
        fields = get_notetype_fields(notetype_id)
        print(fields)

    print(add_field_to_notetype(notetype_dict['Basic'], "More Info"), '\n\n')
    print("changing order: \n")

    notetype_id = notetype_dict['Basic']
    new_order = {
        "Front": 2,
        "Back": 1,
        "More Info": 0  
    }
    result = reorder_notetype_fields(notetype_id, new_order)

    fields = get_notetype_fields(notetype_dict['Basic'])
    print(fields)

    result = set_sort_field(notetype_dict['Basic'], "More Info")
    sort_field = get_sort_field(notetype_id)
    print(sort_field)

    result = set_sort_field(notetype_dict['Basic'], "Front")
    sort_field = get_sort_field(notetype_id)
    print(sort_field)
    
    delete_field_from_note(notetype_dict['Basic'], "More Info")
    print('\n\n')
    notetype_id = notetype_dict['Basic']
    new_order = {
        "Front": 0,
        "Back": 1,
    }
    result = reorder_notetype_fields(notetype_id, new_order)

    fields = get_notetype_fields(notetype_dict['Basic'])
    print(fields)

    print(create_notetype_with_fields("New Notetype", ["Field1", "Field2"], notetype_dict['Basic']), '\n\n')

    notetypes = get_notetypes()
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
            result = delete_notetype_by_id(notetype_dict[notetype])

    notetypes = get_notetypes()
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
            result = delete_notetype_by_id(notetype_dict[notetype])
