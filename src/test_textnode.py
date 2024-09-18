import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_text_to_html(self):
        node = TextNode("I love him so much", text_type_image, "https://preview.redd.it/ruxastys2kfc1.jpg?width=2000&format=pjpg&auto=webp&s=f28b66d36c0b6aab2ac131a91ec667e20e1e3281")
        text = '<img src="https://preview.redd.it/ruxastys2kfc1.jpg?width=2000&format=pjpg&auto=webp&s=f28b66d36c0b6aab2ac131a91ec667e20e1e3281" alt="I love him so much"></img>'
        self.assertEqual(node.text_to_leaf().to_html(), text)

    def test_text_to_html1(self):
        node = TextNode("I love him so much", text_type_italic)
        text = "<i>I love him so much</i>"
        self.assertEqual(node.text_to_leaf().to_html(), text)

    def test_invaldtexttype(self):
        with self.assertRaises(Exception) as context:
            node = TextNode("banananananan", "underline")
            node.text_to_leaf().to_html()
        self.assertEqual(str(context.exception), "invalid text type")

if __name__ == "__main__":
    unittest.main()