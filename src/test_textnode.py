import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Testing None url", TextType.BOLD, None)
        node2 = TextNode("Testing None url", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_neq(self):
        node = TextNode("Test url", TextType.NORMAL, "https://www.oops.com")
        node2 = TextNode("test url", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_type_neq(self):
        node = TextNode("Testing TextType", TextType.NORMAL)
        node2 = TextNode("Testing TextType", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_text_neq(self):
        node = TextNode("Test text", TextType.NORMAL)
        node2 = TextNode("Testing text", TextType.NORMAL)
        self.assertNotEqual(node, node2)
        


if __name__ == "__main__":
    unittest.main()