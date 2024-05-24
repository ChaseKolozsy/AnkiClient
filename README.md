# AnkiClient

AnkiClient is a Python-based client that interacts with Anki to manage decks, cards, media, and user operations. This client provides various functionalities to import, create, view, and manage Anki content programmatically.

## AnkiAPI
[Visit AnkiAPI for the API that this client uses](https://github.com/ChaseKolozsy/AnkiAPI)

## Features

- Import decks and media
- Create new cards
- View existing cards
- Initialize the server for interaction with Anki
- Various operations for managing decks, studies, users, notes, and more

## Directory Structure

```
src/
├── operations/
│   ├── deck_ops.py
│   ├── study_ops.py
│   ├── user_ops.py
│   ├── note_ops.py
│   ├── db_ops.py
│   ├── import_ops.py
│   ├── export_ops.py
│   ├── card_ops.py
```

## Installation

To install the necessary dependencies, run:

```sh
pip install requests 
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

## Usage

Each operation is designed to be used as a module, allowing for easy integration into your own scripts or applications.
Each module has test code in the `if __name__ == "__main__":` block, but these will have to be customized with your own data if you want the tests to function. data should be kept inside of a data directory which should be contained in the root directory of the repository. This is currently designed to assume that the project and the repository are located in the same root directory. 

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
