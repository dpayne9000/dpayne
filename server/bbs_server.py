from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
DATA_FILE = "./data/social_board_data.json"

def load_posts():
    try:
        with open(DATA_FILE, 'r') as file:
            posts = json.load(file)
            return posts if posts else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_posts(posts):
    with open(DATA_FILE, 'w') as file:
        json.dump(posts, file, indent=4)

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = load_posts()
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data.get("author") or not data.get("content"):
        return jsonify({"error": "Invalid data"}), 400

    posts = load_posts()
    new_post = {
        "id": len(posts) + 1,
        "author": data["author"],
        "content": data["content"],
        "comments": [],
        "timestamp": str(datetime.now())
    }
    posts.append(new_post)
    save_posts(posts)

    # Emit the new post event to all connected clients
    socketio.emit('new_post', new_post, broadcast=True)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    data = request.get_json()
    if not data.get("author") or not data.get("content"):
        return jsonify({"error": "Invalid data"}), 400

    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            comment = {
                "author": data["author"],
                "content": data["content"],
                "timestamp": str(datetime.now())
            }
            post["comments"].append(comment)
            save_posts(posts)

            # Emit the new comment event to all connected clients
            socketio.emit('new_comment', {"post_id": post_id, "comment": comment}, broadcast=True)
            return jsonify(comment), 201

    return jsonify({"error": "Post not found"}), 404

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == "__main__":
    socketio.run(app, port=5000, debug=True)
