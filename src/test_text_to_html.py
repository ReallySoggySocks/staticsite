from typing import Text
import unittest

from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType

class TextToHTML(unittest.TestCase):
    def testVE(self):
        node = TextNode("test", "BEAN")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def testText(self):
        pass

    def testBold(self):
        pass

    def testItalic(self):
        pass

    def testCode(self):
        pass

    def testLink(self):
        pass

    def testImage(self):
        pass

    def testNoText(self):
        node = TextNode(None, TextType.TEXT)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()