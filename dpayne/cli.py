import argparse
from dpayne.syntax_trainer import load_questions, start_training


def main():
    parser = argparse.ArgumentParser(
        description="Dpayne CLI: A learning platform for Python programming."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command for "learning"
    learning_parser = subparsers.add_parser("learning", help="Run learning tasks")
    learning_parser.add_argument(
        "topic", choices=["syntax"], help="The learning topic (e.g., syntax)"
    )
    learning_parser.add_argument(
        "lesson_file", help="Path to the lesson file (e.g., questions.json)"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "learning" and args.topic == "syntax":
        questions = load_questions(f'./dpayne/lessons/{args.lesson_file}.json')
        start_training(questions)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
