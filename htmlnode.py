class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        print(self.props)
    
    def __repr__(self):
        print(f"{self.tag}, {self.value}, {self.children}, {self.props}")