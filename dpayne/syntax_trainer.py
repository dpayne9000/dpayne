import json
import random


def load_questions(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return []


def start_training(questions: list) -> None:
    if not questions:
        print("No questions available for training. Please check the data file.")
        return

    print("Welcome to Python Syntax Training!")
    print("You will be presented with common code snippets.")
    print("Your task is to correct the syntax of a given example.")
    print("You will also see a valid example in a different form for guidance.\n")

    random.shuffle(questions)
    for question in questions:
        print(f"Description: {question['description']}")
        print(f"Valid Example:\n{question['valid']}")
        print(f"Incorrect Example:\n{question['incorrect']}")
        user_input = input("Correct this code: ")

        if user_input.strip() == question["correct"].strip():
            print("✅ Correct!\n")
        else:
            print(f"❌ Incorrect. The correct code is:\n{question['correct']}\n")
        print("-" * 50)

    print("Training complete! Keep practicing to improve.")
