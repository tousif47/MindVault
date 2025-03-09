# tests/test_database.py

import unittest
import sqlite3
import os

from utils.database import create_connection
from utils.database import create_tables
from utils.database import insert_document
from utils.database import insert_summary
from utils.database import insert_tags
from utils.database import insert_query


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a temporary database for testing."""
        
        cls.db_file = "test_mindvault.db"
        cls.conn = create_connection(cls.db_file)

        if cls.conn is not None:
            create_tables(cls.conn)
        else:
            raise Exception("Error: Could not connect to the database.")

    @classmethod
    def tearDownClass(cls):
        """Clean up the temporary database after testing."""

        if cls.conn:
            cls.conn.close()

        #if os.path.exists(cls.db_file):
        #    os.remove(cls.db_file)
    
    def test_insert_document(self):
        """Test inserting a document into the database."""

        file_path = "test.pdf"
        extracted_text = "This is a test document."
        document_id = insert_document(self.conn, file_path, extracted_text)
        self.assertIsNotNone(document_id, "Document insertion failed!")
        print(f"Inserted document with ID: {document_id}")
    
    def test_insert_summary(self):
        """Test inserting a summary into the database."""

        document_id = 1 # Assuming the document was inserted in the previous test
        summary_text = "This is a test summary."
        insert_summary(self.conn, document_id, summary_text)
        cursor = self.conn.cursor()
        cursor.execute("SELECT summary_text FROM summaries WHERE document_id = ?", (document_id,))
        result = cursor.fetchone()
        self.assertEqual(result[0], summary_text, "Summary insertion failed!")
        print(f"Inserted summary for document ID: {document_id}")
    
    def test_insert_tags(self):
        """Test inserting tags into the database."""

        document_id = 1 # Assuming the document was inserted in the previous test
        tags = ["tags", "document"]
        insert_tags(self.conn, document_id, tags)
        cursor = self.conn.cursor()
        cursor.execute("SELECT tag_text FROM tags WHERE document_id = ?", (document_id,))
        results = cursor.fetchall()
        retrieved_tags = [result[0] for result in results]  # Extract the tag_text from the list of tuples
        self.assertEqual(sorted(retrieved_tags), sorted(tags), "Tags insertion failed!")    # Sort both lists before comparing
        print(f"Inserted tags for document ID: {document_id}")
    
    def test_insert_query(self):
        """Test inserting a query and its answer into the database."""

        document_id = 1 # Assuming the document was inserted in the previous test
        query_text = "What is this document about?"
        answer_text = "This is a test document."
        insert_query(self.conn, query_text, answer_text, document_id)
        cursor = self.conn.cursor()
        cursor.execute("SELECT answer_text FROM queries WHERE document_id = ?", (document_id,))
        result = cursor.fetchone()
        self.assertEqual(result[0], answer_text, "Query insertion failed!")
        print(f"Inserted query and answer for document ID: {document_id}")


if __name__ == "__main__":
    unittest.main()