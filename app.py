from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for example
BOOKS = [
    {"title": "The Alchemist", "genre": "fiction", "author": "Paulo Coelho", "mood": "motivational", "tag": "spiritual"},
    {"title": "Harry Potter", "genre": "fantasy", "author": "J.K. Rowling", "mood": "exciting", "tag": "magic"},
    {"title": "The Subtle Art of Not Giving a F*ck", "genre": "self-help", "author": "Mark Manson", "mood": "realistic", "tag": "life"},
    {"title": "Atomic Habits", "genre": "self-help", "author": "James Clear", "mood": "motivational", "tag": "habit"}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "endpoints": {
            "/": "This home page",
            "/recommend": "Get book recommendations with optional filters (genre, author, mood, tag, limit)"
        },
        "example": "/recommend?genre=fantasy&limit=2",
        "message": "Welcome to the Book Recommendation API"
    })

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    genre = data.get("genre")
    author = data.get("author")
    mood = data.get("mood")
    tag = data.get("tag")
    limit = int(data.get("limit", 5))

    filtered = BOOKS
    if genre:
        filtered = [book for book in filtered if book["genre"].lower() == genre.lower()]
    if author:
        filtered = [book for book in filtered if book["author"].lower() == author.lower()]
    if mood:
        filtered = [book for book in filtered if book["mood"].lower() == mood.lower()]
    if tag:
        filtered = [book for book in filtered if book["tag"].lower() == tag.lower()]

    return jsonify({"recommendation": filtered[:limit]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
