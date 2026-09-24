import random
import nltk

from nltk.tokenize import word_tokenize

# Download tokenizer data if required
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


# FAQ responses
FAQ_RESPONSES = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi! Welcome to our customer support chatbot.",
        "Hello! What can I help you with?"
    ],

    "hi": [
        "Hi! How can I help you?",
        "Hello! Nice to meet you.",
        "Hi there! What would you like to know?"
    ],

    "good morning": [
        "Good morning! How can I help you?",
        "Good morning! What can I do for you?"
    ],

    "good evening": [
        "Good evening! How can I assist you?"
    ],

    "bye": [
        "Goodbye! Have a great day!",
        "Thank you for chatting with us. Goodbye!",
        "See you again!"
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "No problem!"
    ],

    "thank you": [
        "You're welcome!",
        "Glad I could help!"
    ],

    "course": [
        "We offer various technical and professional courses."
    ],

    "courses": [
        "We offer courses in Python, Java, Web Development, Data Science and AI."
    ],

    "python": [
        "Python is a popular programming language used for web development, AI, data science and automation."
    ],

    "java": [
        "Java is a powerful programming language commonly used for web, mobile and enterprise applications."
    ],

    "timing": [
        "Our support service is available from 9:00 AM to 6:00 PM, Monday to Saturday."
    ],

    "contact": [
        "You can contact our support team through email or phone during working hours."
    ],

    "email": [
        "Please send your query to our official support email."
    ],

    "fees": [
        "Course fees depend on the selected course. Please contact our support team for current fee details."
    ],

    "payment": [
        "We accept common online payment methods such as UPI, cards and net banking."
    ],

    "certificate": [
        "Certificates are provided after successful completion of the course."
    ],

    "help": [
        "I can help you with courses, fees, timings, payments, certificates and contact information."
    ]
}


def find_response(message):
    """
    Generate a chatbot response based on the user's message.
    """

    message = message.lower().strip()

    if not message:
        return "Please type a message so I can help you."

    # Tokenize the message
    try:
        tokens = word_tokenize(message)
    except Exception:
        tokens = message.split()

    # Check exact phrase first
    for keyword, responses in FAQ_RESPONSES.items():
        if keyword in message:
            return random.choice(responses)

    # Check individual words
    for token in tokens:
        if token in FAQ_RESPONSES:
            return random.choice(FAQ_RESPONSES[token])

    # Default response
    return (
        "I'm sorry, I didn't understand that. "
        "You can ask me about courses, fees, payments, "
        "timings, certificates or contact information."
    )