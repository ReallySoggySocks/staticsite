from textnode import TextNode, TextType

node = TextNode("This is a **bold** word", TextType.TEXT)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for word in old_nodes.text.split():
        if delimiter in word:
            text_type = TextType[delimiter]
    
    return text_type