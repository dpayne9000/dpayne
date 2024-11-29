import requests
import os


class BBSClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    def list_posts(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            if response.status_code == 200:
                posts = response.json()
                for post in posts:
                    print(
                        f"Post ID: {post['id']} | Author: {post['author']} | Posted: {post['timestamp']}"
                    )
                    print(f"Content: {post['content']}\n")
            else:
                print("Failed to retrieve posts.")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def create_post(self, author, content):
        data = {"author": author, "content": content}
        try:
            response = requests.post(f"{self.base_url}/posts", json=data)
            if response.status_code == 201:
                print(f"Post by '{author}' added successfully.")
            else:
                print("Failed to create post. Error:", response.json().get("error"))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def add_comment(self, post_id, author, content):
        data = {"author": author, "content": content}
        try:
            response = requests.post(
                f"{self.base_url}/posts/{post_id}/comments", json=data
            )
            if response.status_code == 201:
                print(f"Comment by '{author}' added successfully.")
            else:
                print("Failed to add comment. Error:", response.json().get("error"))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def view_post(self, post_id):
        try:
            response = requests.get(f"{self.base_url}/posts")
            if response.status_code == 200:
                posts = response.json()
                post = next((p for p in posts if p["id"] == post_id), None)
                if post:
                    print(
                        f"Post ID: {post['id']} | Author: {post['author']} | Posted: {post['timestamp']}"
                    )
                    print(f"Content: {post['content']}\n")
                    if post["comments"]:
                        print("Comments:")
                        for comment in post["comments"]:
                            print(
                                f"    Author: {comment['author']} | Posted: {comment['timestamp']}"
                            )
                            print(f"    {comment['content']}\n")
                    else:
                        print("No comments yet.\n")
                else:
                    print("Post not found.")
            else:
                print("Failed to retrieve post.")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


# Example usage of the BBSClient module
if __name__ == "__main__":
    bbs_client = BBSClient()

    while True:
        print("\nBBS Message Board Menu:")
        print("1. Create Post")
        print("2. Add Comment to Post")
        print("3. List All Posts")
        print("4. View Specific Post")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            author = input("Enter your name: ")
            content = input("Enter your post content: ")
            bbs_client.create_post(author, content)
        elif choice == "2":
            try:
                post_id = int(input("Enter the post ID to comment on: "))
                author = input("Enter your name: ")
                content = input("Enter your comment: ")
                bbs_client.add_comment(post_id, author, content)
            except ValueError:
                print("Invalid post ID. Please enter a number.")
        elif choice == "3":
            bbs_client.list_posts()
        elif choice == "4":
            try:
                post_id = int(input("Enter the post ID to view: "))
                bbs_client.view_post(post_id)
            except ValueError:
                print("Invalid post ID. Please enter a number.")
        elif choice == "5":
            print("Exiting the BBS Message Board. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
