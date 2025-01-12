import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    
    def test_none(self):
        node = HTMLNode()
        self.assertIsNone(node.children, node.tag)

    def test_val_prop_none(self):
        node = HTMLNode()
        self.assertIsNone(node.value, node.props)
    
    def test_tag_neq(self):
        node = HTMLNode("tag")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_val_new(self):
        node = HTMLNode(None, "value")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_children_neq(self):
        node = HTMLNode(None, None, "children")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_props_neq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()