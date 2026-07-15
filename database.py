# ==========================================
# ML COPY
# Banco de dados SQLite
# ==========================================

import sqlite3
import os

from config import DATABASE_FILE



def get_connection():

    pasta = os.path.dirname(DATABASE_FILE)

    if pasta and not os.path.exists(pasta):

        os.makedirs(pasta)


    conn = sqlite3.connect(
        DATABASE_FILE
    )

    return conn



def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT,

            nickname TEXT,

            access_token TEXT,

            refresh_token TEXT,

            expires_in INTEGER,

            role TEXT DEFAULT 'donor'

        )
        """
    )


    conn.commit()

    conn.close()