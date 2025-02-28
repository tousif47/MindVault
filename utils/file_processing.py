# utils/file_processing.py

from PyPDF2 import PdfReader
from PIL import Image

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

    return text