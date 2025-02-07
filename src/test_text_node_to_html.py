import unittest

from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

class TestTextToLeaf(unittest.TestCase):
    def test_ValueError(self):
        node = TextNode("Value Error Test", None)
        node.text_node_to_html_node()
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()