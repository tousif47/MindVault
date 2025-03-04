# tests/test_NLP_processing.py

import unittest

from utils.NLP_processing import answer_query
from utils.NLP_processing import text_summary
from utils.NLP_processing import tag_generation


class test(unittest.TestCase):
    def test_answer_query(self):
        context = "Python decorators are functions that modify the behavior of other functions."
        query = "What are Python decorators?"
        answer = answer_query(query, context)
        self.assertNotEqual(answer.strip(), "", "Query answering failed!")
        print("Answer Query Test Passed:", answer)
    
    def test_text_summary(self):
        text = "Python decorators are functions that modify the behavior of other functions..."
        summary = text_summary(text)
        self.assertNotEqual(summary.strip(), "", "Text summariation failed!")
        print("Text Summarizaton Test Passed:", summary)
    
    def test_tag_generation(self):
        text = "Python decorators are functions that modify the behavior of other functions."
        tags = tag_generation(text)
        self.assertNotEqual(tags.strip(), "", "Tag generation failed!")
        print("Tag Generation Test Passed:", tags)


if __name__ == "__main__":
    unittest.main()