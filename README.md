Sure, here is the `README.md` content in a codeblock for easy copying:

```markdown
# AnkiClient

AnkiClient is a Python-based client that interacts with Anki to manage decks, cards, media, and user operations. This client provides various functionalities to import, create, view, and manage Anki content programmatically.

## Features

- Import decks and media
- Create new cards
- View existing cards
- Initialize the server for interaction with Anki
- Various operations for managing decks, studies, users, notes, and more

## Directory Structure

src/
├── Misc. Test Scripts:
|   ├── import_media.py
|   ├── import_decks.py
|   ├── create_card.py
|   ├── initialize_Server.py
|   ├── view_cards.py
├── operations/
│   ├── deck_ops.py
│   ├── study_ops.py
│   ├── user_ops.py
│   ├── note_ops.py
│   ├── db_ops.py
│   ├── import_ops.py
│   ├── export_ops.py
│   ├── card_ops.py

## Installation

To install the necessary dependencies, run:

```sh
pip install requests 
```

## Usage

### Initialize Server

To initialize the server, (modify as you please, temporary for testing)

```sh
python src/initialize_Server.py
```


## Operations

The `operations` directory contains various modules for managing different aspects of Anki:

- `deck_ops.py`: Operations related to decks
- `study_ops.py`: Operations related to study sessions
- `user_ops.py`: User-related operations
- `note_ops.py`: Note-related operations
- `db_ops.py`: Database operations
- `import_ops.py`: Import-related operations
- `export_ops.py`: Export-related operations
- `card_ops.py`: Card-related operations

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
