from flask import Flask, request, jsonify, abort
from flask_socketio import SocketIO
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from flask_talisman import Talisman
from datetime import datetime
import json


# Initialize Flask app and security-related tools
app = Flask(__name__)

# Secure headers with Talisman
Talisman(app)

# Cross-Origin Resource Sharing (CORS) with strict settings
CORS(app, resources={r"/posts/*": {"origins": ["https://your-domain.com"]}})

# Rate limiter to prevent abuse
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])
# SocketIO for real-time features
socketio = SocketIO(
    app, cors_allowed_origins="https://your-domain.com", async_mode="gevent"
)

DATA_FILE = "./data/social_board_data.json"


# Helper Functions
def load_posts():
    try:
        with open(DATA_FILE, "r") as file:
            posts = json.load(file)
            return posts if posts else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    with open(DATA_FILE, "w") as file:
        json.dump(posts, file, indent=4)


# Endpoints
@app.route("/posts", methods=["GET"])
@limiter.limit("10 per minute")
def get_posts():
    posts = load_posts()
    return jsonify(posts)


@app.route("/posts", methods=["POST"])
@limiter.limit("5 per minute")
def create_post():
    # Authentication placeholder - replace with your auth logic
    if not request.headers.get("Authorization"):
        abort(401, description="Unauthorized - Missing Authorization header")

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    author = data.get("author")
    content = data.get("content")

    if not author or not content:
        return jsonify({"error": "Invalid data"}), 400

    # Sanitize inputs to prevent XSS attacks
    author = sanitize_input(author)
    content = sanitize_input(content)

    posts = load_posts()
    new_post = {
        "id": len(posts) + 1,
        "author": author,
        "content": content,
        "comments": [],
        "timestamp": datetime.utcnow().isoformat(),
    }
    posts.append(new_post)
    save_posts(posts)

    # Emit the new post event to all connected clients
    socketio.emit("new_post", new_post, to="/")
    return jsonify(new_post), 201


@app.route("/posts/<int:post_id>/comments", methods=["POST"])
@limiter.limit("5 per minute")
def add_comment(post_id):
    # Authentication placeholder
    # if not request.headers.get("Authorization"):
    #     abort(401, description="Unauthorized - Missing Authorization header")

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    author = data.get("author")
    content = data.get("content")

    if not author or not content:
        return jsonify({"error": "Invalid data"}), 400

    # Sanitize inputs to prevent XSS attacks
    author = sanitize_input(author)
    content = sanitize_input(content)

    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            comment = {
                "author": author,
                "content": content,
                "timestamp": datetime.utcnow().isoformat(),
            }
            post["comments"].append(comment)
            save_posts(posts)

            # Emit the new comment event to all connected clients
            socketio.emit(
                "new_comment", {"post_id": post_id, "comment": comment}, to="/"
            )
            return jsonify(comment), 201

    return jsonify({"error": "Post not found"}), 404


# SocketIO Events
@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


# Security Enhancements
def sanitize_input(value: str) -> str:
    """Sanitize input to prevent XSS attacks."""
    import html

    return html.escape(value)


# We don't call socketio.run() here for production
if __name__ == "__main__":
    # Use this for development testing only
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
