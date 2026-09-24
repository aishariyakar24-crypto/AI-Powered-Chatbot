import sqlite3
from datetime import datetime

DATABASE_NAME = "chatbot.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_conversation(user_message, bot_response):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO conversations
        (user_message, bot_response, created_at)
        VALUES (?, ?, ?)
    """, (
        user_message,
        bot_response,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_conversations():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_message, bot_response, created_at
        FROM conversations
        ORDER BY id DESC
    """)

    conversations = cursor.fetchall()

    connection.close()

    return conversations