import json


def load_visual_flashcards(file_path: str) -> list:
    """Load the visual flashcards from a JSON file."""
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


def display_visual_flashcards(flashcards: list) -> None:
    """Display the visual flashcards interactively."""
    if not flashcards:
        print("No visual flashcards available. Please check the data file.")
        return

    print("Welcome to the Visual Flashcards for Staff Engineer Qualities!")
    print("You will see a quality, an explanation, and a visual representation.\n")

    for card in flashcards:
        print(f"Quality: {card['quality']}")
        print(f"\nExplanation:\n{card['explanation']}")
        print(f"\nVisual Representation:\n{card['visual']}")
        print("\n" + "=" * 50)
        input("Press Enter to see the next flashcard...\n")


if __name__ == "__main__":
    data_file = "staff_engineer_qualities.json"
    cards = load_visual_flashcards(data_file)
    display_visual_flashcards(cards)
