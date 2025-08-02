from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def recommend_books():
    try:
        data = request.get_json()
        
        # Get user-defined variables from Watson
        mood = data.get("mood")
        genre = data.get("genre")
        author = data.get("author")
        tag = data.get("tag")  # optional

        # Dummy logic - replace with your database or real logic
        if mood:
            recommendations = get_books_by_mood(mood)
        elif genre:
            recommendations = get_books_by_genre(genre)
        elif author:
            recommendations = get_books_by_author(author)
        elif tag:
            recommendations = get_books_by_tag(tag)
        else:
            recommendations = ["The Alchemist", "To Kill a Mockingbird", "1984"]

        return jsonify({
            "recommendation": recommendations
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_books_by_mood(mood):
    mood = mood.lower()
    return {
        "happy": ["Eleanor Oliphant Is Completely Fine", "The Rosie Project"],
        "sad": ["A Little Life", "The Fault in Our Stars"],
        "romantic": ["Me Before You", "The Notebook"],
        "motivated": ["Atomic Habits", "Can’t Hurt Me"]
    }.get(mood, ["Tuesdays with Morrie", "The Midnight Library"])


def get_books_by_genre(genre):
    genre = genre.lower()
    return {
        "fiction": ["The Great Gatsby", "Pride and Prejudice"],
        "non-fiction": ["Sapiens", "Educated"],
        "fantasy": ["Harry Potter", "The Hobbit"],
        "sci-fi": ["Dune", "Ender’s Game"]
    }.get(genre, ["To Kill a Mockingbird", "The Catcher in the Rye"])


def get_books_by_author(author):
    author = author.lower()
    return {
        "jk rowling": ["Harry Potter and the Sorcerer’s Stone", "Fantastic Beasts"],
        "paulo coelho": ["The Alchemist", "Brida"],
        "george orwell": ["1984", "Animal Farm"]
    }.get(author, ["Sorry, I couldn't find books by that author."])


def get_books_by_tag(tag):
    tag = tag.lower()
    return {
        "bestseller": ["The Silent Patient", "Verity"],
        "classic": ["Moby Dick", "War and Peace"]
    }.get(tag, ["No tag-based recommendations available."])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
