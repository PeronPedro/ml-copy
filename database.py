# ==========================================
# ML COPY
# Banco de Dados SQLite
# ==========================================

import sqlite3
import os

from config import DATABASE_FILE


def get_connection():

    folder = os.path.dirname(DATABASE_FILE)

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER UNIQUE NOT NULL,

            nickname TEXT NOT NULL,

            access_token TEXT,

            refresh_token TEXT,

            expires_in INTEGER,

            role TEXT DEFAULT 'DESTINATION',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    connection.commit()

    connection.close()