import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_inputs(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com"})
        print(node)