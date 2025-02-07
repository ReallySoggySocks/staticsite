import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_inputs_tohtml(self):
        node = LeafNode("p", "This is a paragraph.", {"href": "https://www.google.com"})
        node2 = LeafNode("p", "This is a paragraph.", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), node2.to_html())

    def test_to_html(self):
        node = LeafNode(None, "This is a paragraph", {"prop": "https://www.prop.com"})
        self.assertIsInstance(node.to_html(), str)
    
    def test_none_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError)
    
    def test_none_tag(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertIsInstance(node.value, str)
