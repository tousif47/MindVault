# utils/file_processing.py

from PyPDF2 import PdfReader
from PIL import Image
from utils.database import create_connection, insert_document

import pytesseract
import speech_recognition as sr


def textExtract_PDF(path):
    """
    Extracts text from a PDF file.
    
    Args:
        path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text.
    """

    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Insert the extracted text into the database
    conn = create_connection("mindvault.db")
    if conn is not None:
        document_id = insert_document(conn, path, text)
        conn.close()
        print(f"Inserted document with ID: {document_id}")
    else:
        print("Error: Could not connect to the database.")

    return text


def textExtract_image(path):
    """
    Extracts text from an image file using Tesseract OCR.
    
    Args:
        file_path (str): Path to the image file.
    
    Returns:
        str: Extracted text.
    """

    image = Image.open(path)
    text = pytesseract.image_to_string(image)

    # Insert the extracted text into the database
    conn = create_connection("mindvault.db")
    if conn is not None:
        document_id = insert_document(conn, path, text)
        conn.close()
        print(f"Inserted document with ID: {document_id}")
    else:
        print("Error: Could not connect to the database.")

    return text


def textExtract_audio(path):
    """
    Extracts text from an audio file using SpeechRecognition.
    
    Args:
        file_path (str): Path to the audio file.
    
    Returns:
        str: Extracted text.
    """

    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)

    # Insert the extracted text into the database
    conn = create_connection("mindvault.db")
    if conn is not None:
        document_id = insert_document(conn, path, text)
        conn.close()
        print(f"Inserted document with ID: {document_id}")
    else:
        print("Error: Could not connect to the database.")

    return text