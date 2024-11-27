import argparse
from dpayne.syntax_trainer import load_questions, start_training
from dpayne.flashcards import load_flashcards, start_flashcards
from dpayne.visual_flashcards import load_visual_flashcards, display_visual_flashcards

LESSONS_DIR = "./dpayne/lessons/"
FLASHCARDS_DIR = "./dpayne/flashcards/"
VISUALCARDS_DIR = './dpayne/visualcards/'

def main():
    parser = argparse.ArgumentParser(
        description="Dpayne CLI: A learning platform for Python programming."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command for "learning"
    learning_parser = subparsers.add_parser("learning", help="Run learning tasks")
    learning_parser.add_argument(
        "topic", choices=["syntax", "flashcards", "visualcards"], help="The learning topic (e.g., syntax)"
    )
    learning_parser.add_argument(
        "lesson_file", help="Path to the lesson file (e.g., questions.json)"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "learning":
        if args.topic == "syntax":
            questions = load_questions(f'{LESSONS_DIR}{args.lesson_file}.json')
            start_training(questions)
        elif args.topic == "flashcards":
            cards = load_flashcards(f'{FLASHCARDS_DIR}{args.lesson_file}.json')
            start_flashcards(cards)
        elif args.topic == "visualcards":
            cards = load_visual_flashcards(f'{VISUALCARDS_DIR}{args.lesson_file}.json')
            display_visual_flashcards(cards)
        else:
            print("Invalid topic. Please choose 'syntax' or 'flashcards'.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
