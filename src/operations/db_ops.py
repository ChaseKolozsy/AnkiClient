import requests


##TODO:
# - Add more tests
# - Add more operations


if __name__ == "__main__":
    from note_ops import get_notetypes
    from user_ops import create_user, delete_user
    from deck_ops import create_deck
    from import_ops import upload_anki_package, upload_csv_file
    from pathlib import Path

    ## ----------------------------------- Initialize ------------------------------------- ##
    username = "User 1"  # Replace with the actual username
    print(create_user(username))
    deck_id = create_deck(deck_name="testdeck", username=username)['id']
    print(deck_id)
    create_deck(deck_name="Hungarian", username=username)

    file_name = '0_Video_Segments.apkg'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/apkgs/{file_name}'
    upload_anki_package(username, file_path)

    notetype = 'Basic' 
    deck_name = 'Hungarian'
    delimiter = 'TAB'

    file_name = 'Food-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)

    file_name = 'Directions-recite.txt'
    file_path = Path.home() / f'Documents/FromX2Ank/AnkiClient/data/csv_files/{file_name}'
    upload_csv_file(username, file_path, deck_name, notetype, delimiter)



    notetypes = get_notetypes(username)
    notetype_dict = {}
    if notetypes:
        print("Notetypes retrieved successfully:")
        for notetype in notetypes:
            print(f"ID: {notetype['id']}, Name: {notetype['name']}")
            notetype_dict[notetype['name']] = notetype['id']
    else:
        print("Failed to retrieve notetypes.")