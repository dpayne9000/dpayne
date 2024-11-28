import argparse
from colorama import Fore, Style, init
from dpayne.syntax_trainer import load_questions, start_training
from dpayne.flashcards import load_flashcards, start_flashcards
from dpayne.visual_flashcards import load_visual_flashcards, display_visual_flashcards
from dpayne.games.timewarp import main as timewarp_main

LESSONS_DIR = "./dpayne/lessons/"
FLASHCARDS_DIR = "./dpayne/flashcards/"
VISUALCARDS_DIR = './dpayne/visualcards/'

def display_ascii_art():
    print(Fore.GREEN + r"""
      ___           ___           ___           ___           ___           ___     
     /\  \         /\  \         /\  \         |\__\         /\__\         /\  \    
    /::\  \       /::\  \       /::\  \        |:|  |       /::|  |       /::\  \   
   /:/\:\  \     /:/\:\  \     /:/\:\  \       |:|  |      /:|:|  |      /:/\:\  \  
  /:/  \:\__\   /::\~\:\  \   /::\~\:\  \      |:|__|__   /:/|:|  |__   /::\~\:\  \ 
 /:/__/ \:|__| /:/\:\ \:\__\ /:/\:\ \:\__\     /::::\__\ /:/ |:| /\__\ /:/\:\ \:\__\
 \:\  \ /:/  / \/__\:\/:/  / \/__\:\/:/  /    /:/~~/~    \/__|:|/:/  / \:\~\:\ \/__/
  \:\  /:/  /       \::/  /       \::/  /    /:/  /          |:/:/  /   \:\ \:\__\  
   \:\/:/  /         \/__/        /:/  /     \/__/           |::/  /     \:\ \/__/  
    \::/__/                      /:/  /                      /:/  /       \:\__\    
     ~~                          \/__/                       \/__/         \/__/    
    """ + Style.RESET_ALL)

def main():
    init()
    display_ascii_art()
    parser = argparse.ArgumentParser(
        description="Dpayne CLI: A learning platform for Python programming.\n\n"
                    "ex: dpayne learning flashcards listcomprehension\n"
                    "dpayne learning syntax python3\n\n"
                    "For more information, use 'dpayne <command> --help'.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command for "games"
    games_parser = subparsers.add_parser("games", help="Games to help you get pumped up!")
    
    games_parser.add_argument(
        "topic", choices=["timewarp"], help="The game to play (e.g., timewarp)"
    )

    # Sub-command for "learning"
    learning_parser = subparsers.add_parser("learning", help="Run learning tasks")
    learning_parser.add_argument(
        "topic", choices=["syntax", "flashcards", "visualcards"], help="The learning tool to use (e.g., syntax)"
    )
    learning_parser.add_argument(
        "lesson_file", help="Path to the lesson file with no extension (e.g., python1)"
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
    elif args.command == "games":
        if args.topic == "timewarp":
            timewarp_main()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
