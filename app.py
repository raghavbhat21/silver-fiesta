import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recommend_books():
    try:
        data = request.get_json()
        print("Received data:", data)

        # Watson sends context inside 'context' or 'input'; adjust as needed
        intent = data.get("intent", "")
        mood = data.get("mood", "")

        if intent == "recommend_by_mood":
            recommendations = {
                "happy": ["The Alchemist", "The Little Prince", "Eat Pray Love"],
                "sad": ["Man's Search for Meaning", "A Man Called Ove", "The Fault in Our Stars"],
                "romantic": ["Pride and Prejudice", "Me Before You", "The Notebook"],
                "anxious": ["The Power of Now", "Atomic Habits", "Can't Hurt Me"]
            }

            books = recommendations.get(mood.lower(), ["Ikigai", "The Subtle Art of Not Giving a F*ck", "Deep Work"])
            response_text = f"Here are some great books for your mood ({mood}): {', '.join(books)}"

            return jsonify({
                "recommendation": response_text
            })

        else:
            return jsonify({
                "recommendation": "Sorry, I couldn't understand the mood you're in."
            })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "recommendation": "Something went wrong while processing your request."
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


