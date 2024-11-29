from .modules.converser import Converser
import os


def get_api_key():
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    return api_key


def main():
    api_key = get_api_key()
    gpt = Converser(api_key)

    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break
        response = gpt.get_response(user_input)
        print(f"ChatGPT: {response}")
