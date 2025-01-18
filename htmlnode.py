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

class LeafNode:
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        formatted = ""
        if self.props != None:
            for item in self.props:
                value = self.props[item]
                formatted += f' {item}="{value}"'
            return formatted

        if self.value == None:
            raise ValueError("All LeafNodes must have a value")
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {formatted}>{self.value}</{self.tag}>"

class ParentNode:
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All ParentNodes must have a tag")
        if self.children == None:
            raise ValueError("All ParentNodes must have children")
        if not isinstance(self.children, list):
            raise ValueError("Children must be in a list")
        else:
            children_tag = ""

            for child in self.children:
                children_tag += child.to_html()

        # return a string representing the HTML tag of the node and it's children
        return f"<{self.tag}>" + children_tag + f"</{self.tag}>"