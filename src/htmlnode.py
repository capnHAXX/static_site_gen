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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf has no value")
        
        if self.tag is None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        conversion_list = []
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        for child in self.children:
            child_html = child.to_html()
            conversion_list.append(child_html)

        html_string = "".join(conversion_list)
        
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"  