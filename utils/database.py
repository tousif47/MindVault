# utils/database.py

from datetime import datetime

import sqlite3


def create_connection(db_file):
    """
    Craete a database connection to the SQLite database.

    Args:
        db_file (str): Path to the SQLite database file.
    
    Returns:
        sqlite3.Connection: Connection object or None.
    """

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to SQLite databse at {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to databse: {e}")
    
    return connection


def create_tables(connection):
    """
    Create the necessary tables in the database.

    Args:
        connection (sqlite3.Connection): Database connection object.
    """

    sql_create_documents_table = """
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL UNIQUE,
        extracted_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    sql_create_summaries_table = """
    CREATE TABLE IF NOT EXISTS summaries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL,
        summary_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (document_id) REFERENCES documents (id)
    );
    """

    sql_create_tags_table = """
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL,
        tag_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (document_id) REFERENCES documents (id)
    );
    """

    sql_create_queries_table = """
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_text TEXT NOT NULL,
        answer_text TEXT NOT NULL,
        document_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (document_id) REFERENCES documents (id)
    );
    """
    # TODO: implement try/except for table creation


def insert_document():
    # TODO


def insert_summary():
    # TODO


def insert_tags():
    # TODO


def insert_query():
    # TODO