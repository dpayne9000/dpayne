from openai import OpenAI
import os

if os.environ.get('OPENAI_API_KEY') is None:
    print("OPENAI_API_KEY environment variable not set. Please set it before running the script.")
    exit(1)

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


class Converser:
    def __init__(self):
        self.conversation = []  # To store conversation history

    def add_message(self, role, content):
        """Add a message to the conversation."""
        self.conversation.append({"role": role, "content": content})

    def get_response(self, prompt, model="gpt-3.5-turbo", max_tokens=150):
        """Get a response from the model."""
        self.add_message("user", prompt)
        try:
            response = client.chat.completions.create(
                model=model,
                messages=self.conversation,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            message_content = response.choices[0].message.content
            self.add_message("assistant", message_content)
            return message_content
        except Exception as e:
            return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key
    gpt = Converser()
    
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting... Goodbye!")
            break
        response = gpt.get_response(user_input)
        print(f"ChatGPT: {response}")
