from openai import OpenAI
import os


class Converser:
    def __init__(self, api_key):
        self.conversation = []  # To store conversation history
        self.validate()
        api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def validate(self):
        if os.environ.get("OPENAI_API_KEY") is None:
            print(
                "OPENAI_API_KEY environment variable not set. Please set it before running the script."
            )
            exit(1)

    def add_message(self, role, content):
        """Add a message to the conversation."""
        self.conversation.append({"role": role, "content": content})

    def get_response(self, prompt, model="gpt-3.5-turbo", max_tokens=150):
        """Get a response from the model."""
        self.add_message("user", prompt)
        try:
            response = self.client.chat.completions.create(
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
    api_key = ""
    gpt = Converser()

    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break
        response = gpt.get_response(user_input)
        print(f"ChatGPT: {response}")
