import json
import webbrowser


def load_flashcards(file_path: str) -> list:
    """Load the flashcards from a JSON file."""
    try:
        with open(file_path, "r") as file:
            flashcards = json.load(file)
        return flashcards
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return []


def start_flashcards(flashcards: list) -> None:
    """Start the flashcards session with the provided cards."""
    if not flashcards:
        print("No flashcards available. Please check the data file.")
        return

    print("Welcome to Python Flash Cards!")
    print("You will be shown a concept name, explanation, and example code.")
    print("Press 'l' to learn more online, 'n' to view the next card, or 'q' to quit.\n")

    for card in flashcards:
        print(f"Concept: {card['concept']}")
        print(f"\nExplanation:\n{card['explanation']}")
        print(f"\nExample Code:\n{card['example']}\n")
        print("-" * 50)

        while True:
            action = input("Press 'l' for Google search, 'n' for next card, or 'q' to quit: ").strip().lower()
            if action == 'l':
                open_google_search(card['concept'])
            elif action == 'n':
                break
            elif action == 'q':
                print("Exiting Flash Cards. Happy learning!")
                return
            else:
                print("Invalid input. Please press 'l', 'n', or 'q'.")
        print("\n" + "=" * 50 + "\n")


def open_google_search(query: str) -> None:
    """Open a Google search for the given query."""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    print(f"Opening browser for: {search_url}")
    webbrowser.open(search_url)


if __name__ == "__main__":
    data_file = "./flashcards/python1.json"
    cards = load_flashcards(data_file)
    start_flashcards(cards)
