from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = None
    BOLD = "**"
    ITALIC = "*"
    CODE = "```"
    LINKS = "[]"
    IMAGES = "![]"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self):
        if self.text_type == TextType.NORMAL:
            new_node = LeafNode(None, self)
            return new_node
            
        elif self.text_type == TextType.BOLD:
            new_node = LeafNode("b", self.text)
            return new_node
            
        elif self.text_type == TextType.ITALIC:
            new_node = LeafNode("i", self.text)
            return new_node
            
        elif self.text_type == TextType.CODE:
            new_node = LeafNode("code", self.text)
            return new_node
            
        elif self.text_type == TextType.LINKS:
            new_node = LeafNode("a", self.text, {"href" : f"{self.url}"})
            return new_node
            
        elif self.text_type == TextType.IMAGES:
            new_node = LeafNode("img", None, {"src" : f"{self.url}", "alt" : f"{self.text}"})
            return new_node
        
        else:
            raise ValueError("Invalid Text Type")
    
    def __eq__(self, node2):
        if self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


