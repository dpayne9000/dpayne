from .modules.converser import Converser

def main(api_key):
    gpt = Converser(api_key)
    
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting... Goodbye!")
            break
        response = gpt.get_response(user_input)
        print(f"ChatGPT: {response}")