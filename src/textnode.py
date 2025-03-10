from enum import Enum

class TextType(Enum):
    TEXT = None
    BOLD = "**"
    ITALIC = "*"
    CODE = "```"
    LINK = "[]"
    IMAGE = "![]"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node2):
        if self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


