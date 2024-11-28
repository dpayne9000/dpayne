import argparse
import curses
from colorama import Fore, Style, init
from dpayne.syntax_trainer import load_questions, start_training
from dpayne.flashcards import load_flashcards, start_flashcards
from dpayne.visual_flashcards import load_visual_flashcards, display_visual_flashcards
from dpayne.games.timewarp import main as timewarp_main
from dpayne.music.drums.runtime import main as drums_main
from dpayne.converse import main as converse_main
from .social import main as bbs_main

LESSONS_DIR = "./dpayne/lessons/"
FLASHCARDS_DIR = "./dpayne/flashcards/"
VISUALCARDS_DIR = "./dpayne/visualcards/"


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
    display_ascii_art()
    parser = argparse.ArgumentParser(
        description="Dpayne CLI: A learning platform for Python programming.\n\n"
                    "ex: dpayne learning flashcards listcomprehension\n"
                    "dpayne ai chatgpt\n"
                    "dpayne learning syntax python3\n\n"
                    "For more information, use 'dpayne <command> --help'.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    social_parser = subparsers.add_parser("social", help="Ai Help Tools")
    social_parser.add_argument(
        "topic", choices=["bbs", "irc"], help="The music tools (e.g., drums)"
    )

    ai_parser = subparsers.add_parser("ai", help="Ai Help Tools")
    ai_parser.add_argument(
        "topic", choices=["chatgpt"], help="The music tools (e.g., drums)"
    )

    music_parser = subparsers.add_parser("music", help="Music creation tools")
    music_parser.add_argument(
        "topic", choices=["drums"], help="The music tools (e.g., drums)"
    )

    games_parser = subparsers.add_parser("games", help="Games to help you get pumped up!")
    games_parser.add_argument(
        "topic", choices=["timewarp"], help="The game to play (e.g., timewarp)"
    )

    learning_parser = subparsers.add_parser("learning", help="Run learning tasks")
    learning_parser.add_argument(
        "topic", choices=["syntax", "flashcards", "visualcards"], help="The learning tool to use (e.g., syntax)"
    )
    learning_parser.add_argument(
        "lesson_file", help="Path to the lesson file with no extension (e.g., python1)"
    )

    args = parser.parse_args()

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
            print("Playing Timewarp!")
            timewarp_main()
    elif args.command == "music":
        if args.topic == "drums":
            curses.wrapper(drums_main)
    elif args.command == "ai":
        if args.topic == "chatgpt":
            converse_main()
    elif args.command == "social":
        if args.topic == "bbs":
            bbs_main()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
