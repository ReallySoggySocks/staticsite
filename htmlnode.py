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
        formatted = ""
        if self.props != None:
            for item in self.props:
                value = self.props[item]
                formatted += f' {item}="{value}"'
        return formatted
    
    def __repr__(self):
        print(f"{self.tag}, {self.value}, {self.children}, {self.props}")

def text_node_to_html_node(text_node):
    type_dict = {TextType.TEXT : None, TextType.BOLD : "b", TextType.ITALIC : 'i', TextType.CODE : "code", TextType.LINK : "a", TextType.IMAGE : "img"}
    text_node_type = None

    for type in type_dict:
        if text_node.text_type == type:
            text_node_type = type_dict[type]
            return text_node_type
        if type == type_dict[TextType.LINK]:
            text_url = {"href" : f"{text_node.url}"}
            return text_url
        if type == type_dict[TextType.IMAGE]:
            text_url = {"src" : f"{text_node.url}", "alt" : f"{text_node.text}"}
            return text_url
        else:
            raise ValueError
    
    new_node = LeafNode(text_node_type, text_node.text, text_url)
    return new_node

class LeafNode:
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
    
        if value is None:
            raise ValueError("All LeafNodes Must Have A Value")
    
    def to_html(self):
        formatted = ""
        if self.props != None:
            for item in self.props:
                value = self.props[item]
                formatted += f' {item}="{value}"'
            return formatted

        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {formatted}>{self.value}</{self.tag}>"

class ParentNode:
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

        if self.tag == None:
            raise ValueError("All ParentNodes must have a tag")
        if self.children == None:
            raise ValueError("All ParentNodes must have children")
        if not isinstance(self.children, list):
            raise ValueError("Children must be in a list")
    
    def to_html(self):
        children_tag = ""

        for child in self.children:
            children_tag += child.to_html()

        # return a string representing the HTML tag of the node and it's children
        return f"<{self.tag}>" + children_tag + f"</{self.tag}>"