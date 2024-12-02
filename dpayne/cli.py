import argparse
import curses
from colorama import Fore, Style
from typing import Optional


from dpayne.syntax_trainer import load_questions, start_training
from dpayne.flashcards import load_flashcards, start_flashcards
from dpayne.visual_flashcards import load_visual_flashcards, display_visual_flashcards
from dpayne.games.timewarp import main as timewarp_main
from dpayne.music.drums.runtime import main as drums_main
from dpayne.converse import main as converse_main
from .social import main as bbs_main
from .modules.irc_client import main as irc_main

LESSONS_DIR: str = "./dpayne/lessons/"
FLASHCARDS_DIR: str = "./dpayne/flashcards/"
VISUALCARDS_DIR: str = "./dpayne/visualcards/"


def display_ascii_art() -> None:
    print(
        Fore.GREEN
        + r"""
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
    """
        + Style.RESET_ALL
    )


import argparse
from colorama import Fore, Style
from dpayne.syntax_trainer import load_questions, start_training
from dpayne.flashcards import load_flashcards, start_flashcards
from dpayne.visual_flashcards import load_visual_flashcards, display_visual_flashcards
from dpayne.games.timewarp import main as timewarp_main
from dpayne.music.drums.runtime import main as drums_main
from dpayne.converse import main as converse_main
from dpayne.modules.http_requester import HttpRequester
from .social import main as bbs_main

LESSONS_DIR: str = "./dpayne/lessons/"
FLASHCARDS_DIR: str = "./dpayne/flashcards/"
VISUALCARDS_DIR: str = "./dpayne/visualcards/"


# Handlers for each command
def handle_learning(topic: str, lesson_file: str) -> None:
    if topic == "syntax":
        questions = load_questions(f"{LESSONS_DIR}{lesson_file}.json")
        start_training(questions)
    elif topic == "flashcards":
        cards = load_flashcards(f"{FLASHCARDS_DIR}{lesson_file}.json")
        start_flashcards(cards)
    elif topic == "visualcards":
        cards = load_visual_flashcards(f"{VISUALCARDS_DIR}{lesson_file}.json")
        display_visual_flashcards(cards)
    else:
        print("Invalid topic. Please choose 'syntax', 'flashcards', or 'visualcards'.")


def handle_games(topic: str) -> None:
    if topic == "timewarp":
        print("Playing Timewarp!")
        timewarp_main()


def handle_music(topic: str) -> None:
    if topic == "drums":
        curses.wrapper(drums_main)


def handle_ai(topic: str) -> None:
    if topic == "chatgpt":
        converse_main()


def handle_social(topic: str) -> None:
    if topic == "bbs":
        bbs_main()
    elif topic == "irc":
        irc_main()



def handle_tools(topic: str) -> None:
    if topic == "http":
        requester = HttpRequester()
        requester.start_ui()


# Command dispatcher
def dispatch_command(args: argparse.Namespace) -> None:
    if args.command == "learning":
        handle_learning(args.topic, args.lesson_file)
    elif args.command == "games":
        handle_games(args.topic)
    elif args.command == "music":
        handle_music(args.topic)
    elif args.command == "ai":
        handle_ai(args.topic)
    elif args.command == "social":
        handle_social(args.topic)
    elif args.command == "tools":
        handle_tools(args.topic)
    else:
        print(
            "Unknown command. Please use 'dpayne <command> --help' for more information."
        )


def main() -> None:
    display_ascii_art()
    parser = argparse.ArgumentParser(
        description="Dpayne CLI: A learning platform for Python programming.\n\n"
        "ex: dpayne learning flashcards listcomprehension\n"
        "dpayne ai chatgpt\n"
        "dpayne learning syntax python3\n\n"
        "For more information, use 'dpayne <command> --help'.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    # Social command
    social_parser = subparsers.add_parser("social", help="Old Timey Social Media Tools")
    social_parser.add_argument(
        "topic",
        choices=["bbs", "irc"],
        help="Old school communication devices (e.g., BBS)",
    )

    # AI command
    ai_parser = subparsers.add_parser("ai", help="AI Help Tools")
    ai_parser.add_argument(
        "topic", choices=["chatgpt"], help="AI tools (e.g., ChatGPT)"
    )

    # Music command
    music_parser = subparsers.add_parser("music", help="Music creation tools")
    music_parser.add_argument(
        "topic", choices=["drums"], help="The music tools (e.g., drums)"
    )

    # Games command
    games_parser = subparsers.add_parser(
        "games", help="Games to help you get pumped up!"
    )
    games_parser.add_argument(
        "topic", choices=["timewarp"], help="The game to play (e.g., Timewarp)"
    )

    # Learning command
    learning_parser = subparsers.add_parser("learning", help="Run learning tasks")
    learning_parser.add_argument(
        "topic",
        choices=["syntax", "flashcards", "visualcards"],
        help="The learning tool to use (e.g., syntax)",
    )
    learning_parser.add_argument(
        "lesson_file", help="Path to the lesson file with no extension (e.g., python1)"
    )

    # Tools command
    tools_parser = subparsers.add_parser(
        "tools", help="Tools to help you get stuff done!"
    )
    tools_parser.add_argument(
        "topic", choices=["http"], help="The tool to use (e.g., http)"
    )
    

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        dispatch_command(args)


if __name__ == "__main__":
    main()
    quit()