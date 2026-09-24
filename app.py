from flask import Flask, render_template, request, jsonify

from chatbot import find_response
from database import create_database, save_conversation


app = Flask(__name__)


# Create database when application starts
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({
            "response": "Please send a message."
        })


    user_message = data.get("message", "").strip()


    if not user_message:
        return jsonify({
            "response": "Please type a message."
        })


    # Generate chatbot response
    bot_response = find_response(user_message)


    # Save conversation
    save_conversation(user_message, bot_response)


    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )