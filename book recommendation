from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genres": ["fantasy", "adventure", "children"],
        "description": "A fantasy adventure about Bilbo Baggins...",
        "tags": ["middle-earth", "dragons", "dwarves", "magic", "quest"],
        "publication_year": 1937,
        "rating": 4.3,
        "mood": "adventurous"
    },
    # Add more books here if needed
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Book Recommendation API",
        "endpoints": {
            "/": "This home page",
            "/recommend": "Get book recommendations with optional filters (genre, author, mood, tag, limit)"
        },
        "example": "/recommend?genre=fantasy&limit=2"
    })

@app.route("/recommend")
def recommend():
    genre = request.args.get("genre")
    author = request.args.get("author")
    mood = request.args.get("mood")
    tag = request.args.get("tag")
    try:
        limit = int(request.args.get("limit", 1))
        if limit <= 0:
            raise ValueError
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Invalid parameter value",
            "message": "Limit must be a positive integer"
        }), 400

    filtered_books = books

    if genre:
        filtered_books = [b for b in filtered_books if genre.lower() in [g.lower() for g in b["genres"]]]
    if author:
        filtered_books = [b for b in filtered_books if author.lower() in b["author"].lower()]
    if mood:
        filtered_books = [b for b in filtered_books if b.get("mood", "").lower() == mood.lower()]
    if tag:
        filtered_books = [b for b in filtered_books if tag.lower() in [t.lower() for t in b["tags"]]]

    filtered_books = filtered_books[:limit]

    if not filtered_books:
        return jsonify({
            "recommendation": "Sorry, I couldn't find any books matching your criteria."
        })

    top_book = filtered_books[0]
    message = f"Here's a good {mood} book: *{top_book['title']}* by {top_book['author']} ({top_book['publication_year']}). {top_book['description']}"

    return jsonify({
        "recommendation": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
