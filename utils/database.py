# utils/database.py

import sqlite3

from datetime import datetime


def create_connection(db_file):
    """
    Craete a database connection to the SQLite database.

    Args:
        db_file (str): Path to the SQLite database file.
    
    Returns:
        sqlite3.Connection: Connection object or None.
    """

    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite databse at {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to databse: {e}")
    
    return conn


def create_tables(conn):
    """
    Create the necessary tables in the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
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
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_documents_table)
        cursor.execute(sql_create_summaries_table)
        cursor.execute(sql_create_tags_table)
        cursor.execute(sql_create_queries_table)
        conn.commit()

        print("Tables created successfully!")
    
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")


def insert_document(conn, file_path, extracted_text):
    """
    Insert a new document into the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
        file_path (str): Path to the file.
        extracted_text (str): Extracted text from the file.
    
    Returns:
        int: ID of the inserted document.
    """

    sql = """
    INSERT INTO documents (file_path, extracted_text)
    VALUES (?, ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql, (file_path, extracted_text))
    conn.commit()

    return cursor.lastrowid


def insert_summary(conn, document_id, summary_text):
    """
    Insert a summary into the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
        document_id (int): ID of the document.
        summary_text (str): Summary of the document.
    """

    sql = """
    INSERT INTO summaries (document_id, summary_text)
    VALUES (?, ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql, (document_id, summary_text))
    conn.commit()


def insert_tags(conn, document_id, tags):
    """
    Insert tags into the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
        document_id (int): ID of the document.
        tags (list): List of tags to insert.
    """

    cursor = conn.cursor()

    # Remove duplications from the tags list
    unique_tags = list(set(tags))

    # Insert only unique tags
    for tag in unique_tags:
        # Check if the tag already exists for this document
        cursor.execute("SELECT id FROM tags WHERE document_id = ? AND tag_text = ?", (document_id, tag))
        if not cursor.fetchone():   # If the tag doesn't exist, insert it
            cursor.execute("INSERT INTO tags (document_id, tag_text) VALUES (?, ?)", (document_id, tag))
    
    conn.commit()


def insert_query(conn, query_text, answer_text, document_id):
    """
    Insert a query and its answer into the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
        query_text (str): The user's query.
        answer_text (str): The generated answer.
        document_id (int): ID of the document.
    """

    sql = """
    INSERT INTO queries (query_text, answer_text, document_id)
    VALUES (?, ?, ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql, (query_text, answer_text, document_id))
    conn.commit()