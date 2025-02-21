import unittest

from htmlnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TextToHTML(unittest.TestCase):
    def testVE(self):
        node = TextNode("test", "BEAN")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def testOutput(self):
        node = TextNode("test", TextType.TEXT)
        self.assertIsInstance(text_node_to_html_node(node), LeafNode)

    def testText(self):
        node = TextNode("test", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node).to_html(), "test")

    def testTypes(self):
        node = TextNode("test", TextType.BOLD)
        node1 = TextNode("test", TextType.ITALIC)
        node2 = TextNode("test", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>test</b>")
        self.assertEqual(text_node_to_html_node(node1).to_html(), "<i>test</i>")
        self.assertEqual(text_node_to_html_node(node2).to_html(), "<code>test</code>")

    def testLinks(self):
        node = TextNode("test", TextType.LINK, "https://www.test.com")
        node1 = TextNode("test image", TextType.IMAGE, "https://www.image.com/some.png")
        self.assertEqual(text_node_to_html_node(node).to_html(), '<a href="https://www.test.com">test</a>')
        self.assertEqual(text_node_to_html_node(node1).to_html(), '<img src="https://www.image.com/some.png" alt="test image">')

    def testNoText(self):
        node = TextNode(None, TextType.TEXT)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()