# tests/test_file_processing.py

import unittest

from utils.file_processing import textExtract_image
from utils.file_processing import textExtract_audio
from utils.file_processing import textExtract_PDF


class test(unittest.TestCase):
    def testImage(self):
        image_text = textExtract_image("F:/Bork/Self/MindVault/tests/data/Test image.jpg")
        print(image_text)
        self.assertNotEqual(image_text.strip(), "", "Image text extraction failed!")
    
    def testAudio(self):
        audio_text = textExtract_audio("F:/Bork/Self/MindVault/tests/data/Test audio.wav")
        print(audio_text)
        self.assertNotEqual(audio_text.strip(), "", "Image text extraction failed!")
    
    def testPDF(self):
        PDF_text = textExtract_PDF("F:/Bork/Self/MindVault/tests/data/Test PDF.pdf")
        print(PDF_text)
        self.assertNotEqual(PDF_text.strip(), "", "Image text extraction failed!")


if __name__ == "__main__":
    unittest.main()