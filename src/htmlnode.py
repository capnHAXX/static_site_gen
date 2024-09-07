class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        def html_prop(item):
            key, value = item
            return f" {key}={value}"
        html_map = map(html_prop, self.props.items())
        html_string = "".join(html_map)
        return html_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children},{self.props_to_html()})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf has no value")
        
        if self.tag == None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"