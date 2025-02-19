import unittest

from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, text_node_to_html_node

class TestTextToLeaf(unittest.TestCase):
    def test_ValueError(self):
        node = TextNode("Text", None)
        text_node_to_html_node(node)
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()