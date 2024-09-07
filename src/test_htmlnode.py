import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", 
                        "This is an HTML node", 
                        [], 
                        {"target": "_blank",})
        self.assertEqual(node.__repr__(), "HTMLNode(a, This is an HTML node, [], target=_blank)")
    
    def test_repr1(self):
        node = HTMLNode("a", 
                        "This is an HTML node", 
                        ['c1','c2'], 
                        {"target": "_blank",})
        self.assertEqual(node.__repr__(), "HTMLNode(a, This is an HTML node, ['c1', 'c2'], target=_blank)")
    
    def test_repr2(self):
        node = HTMLNode("a", 
                        "This is an HTML node", 
                        ['c1','c2'])
        self.assertEqual(node.__repr__(), "HTMLNode(a, This is an HTML node, ['c1', 'c2'],)")
    
    def test_prop_to_html(self):
        node = HTMLNode("a", 
                        "Garry come home", 
                        None,
                        {"href": "https://www.google.com", "target": "_blank"}
                        )
        self.assertEqual(node.props_to_html(), " href=https://www.google.com target=_blank")

class TestLeafNode(unittest.TestCase):
    def test_tohtml(self):
        node = LeafNode(None, "BASEBALL",None,None)
        self.assertEqual(node.to_html(), "BASEBALL")
    
    def test_tohtml2(self):
        node = LeafNode("b", "BASEBALL",None,None)
        self.assertEqual(node.to_html(), "<b>BASEBALL</b>")
   
    def test_tohtml3(self):
        node = LeafNode("a", "BASEBALL",None,{"href": "https://www.mlb.com"})
        self.assertEqual(node.to_html(), "<a href=https://www.mlb.com>BASEBALL</a>")
    
    def test_tohtml4(self):
        node = LeafNode(None, "BASEBALL",None,{"href": "https://www.mlb.com"})
        self.assertEqual(node.to_html(), "BASEBALL")


if __name__ == "__main__":
    unittest.main()