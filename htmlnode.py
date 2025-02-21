
from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is not None:
            formatted = [f' {item}="{value}"' for item, value in self.props.items()]
            return "".join(formatted)
        return ""
    
    def __repr__(self):
        print(f"{self.tag}, {self.value}, {self.children}, {self.props}")

type_dict = {
    TextType.TEXT : (None, None), 
    TextType.BOLD : ("b", None), 
    TextType.ITALIC : ('i', None), 
    TextType.CODE : ("code", None), 
    TextType.LINK : ("a", {"href" : "url"}), 
    TextType.IMAGE : ("img", {"src": "url", "alt": "text"})
    }

def text_node_to_html_node(text_node):
    
    if text_node.text_type not in type_dict:
        raise ValueError("Invalid Text TYpe")
    
    tag, props = type_dict[text_node.text_type]

    if props:
        prop = {k: getattr(text_node, v) for k, v in props.items()}
    else:
        prop = None
    
    return LeafNode(tag, text_node.text, prop)


class LeafNode:
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
    
        if value is None:
            raise ValueError("All LeafNodes Must Have A Value")
    
    def to_html(self):
        formatted = ""
        
        if self.props:
            formatted = " ".join(f'{item}="{value}"' for item, value in self.props.items())
        
        if self.tag == "img":
            return f"<{self.tag} {formatted}>"

        if self.tag is None:
            return self.value
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {formatted}>{self.value}</{self.tag}>"

class ParentNode:
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

        if tag is None:
            raise ValueError("All ParentNodes must have a tag")
        if self.children is None or not isinstance(children, list):
            raise ValueError("All ParentNodes must have children and be in a list")
    
    def to_html(self):
        children_tag = "".join(child.to_html() for child in self.children)

        # return a string representing the HTML tag of the node and it's children
        return f"<{self.tag}>" + children_tag + f"</{self.tag}>"