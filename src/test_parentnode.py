import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_nonetag(self):
        with self.assertRaises(ValueError):
            child = LeafNode(None, "This is a LeafNode", None)
            node = ParentNode(None, child, None)
    
    def test_nonechild(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None, None)
    
    def test_not_list(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", LeafNode(None, "Normal Text"))
    
    def test_output_str(self):
        node = ParentNode("p", 
                          [LeafNode("b", "Bold Text"),
                           LeafNode(None, "Normal Text"),
                           LeafNode("i", "Italic Text"),
                           LeafNode(None, "Normal Text"),
                           ],
                        )
        self.assertIsInstance(node.to_html(), str)

    def test_parent_in_parent(self):
        node = ParentNode("p", [LeafNode("b", "Bold Text")])
        node2 = ParentNode("p", [node])
        self.assertIsInstance(node2.to_html(), str)

    def test_parent_and_leaf_child(self):
        node = ParentNode("p", [LeafNode("b", "Bold Text")])
        node2 = ParentNode("p", [node, LeafNode(None, "Normal Text")])
        node3 = ParentNode("p", [node2, LeafNode("i", "Italic Text")])
        self.assertIsInstance(node3.to_html(), str)