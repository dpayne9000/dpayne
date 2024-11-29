from .modules.bbs_client import BBSClient


def main():
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
