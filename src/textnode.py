url = None
text = None

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


valid_types = {
    "text":None,
    "bold":"b",
    "italic":"i",
    "code":"code",
    "link":("a",{"href":{url}}),
    "image":("img",{"src":{url}, "alt":{text}})
}

from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_to_leaf(self):
        if self.text_type in valid_types:
            
            if self.text_type == "link":
                tag, prop_builder = valid_types[self.text_type]
                prop = prop_builder.copy()
                prop["href"] = self.url
                leaf_node = LeafNode(tag, self.text, prop)
            
            elif self.text_type == "image":
                tag, prop_builder = valid_types[self.text_type]
                prop = prop_builder.copy()
                prop["src"] = self.url
                prop["alt"] = self.text
                leaf_node = LeafNode(tag, "", prop)
            
            else:
                tag = valid_types[self.text_type]
                leaf_node = LeafNode(tag, self.text)
            
            return leaf_node
        else:
            raise Exception("invalid text type")
