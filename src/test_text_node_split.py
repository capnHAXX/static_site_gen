import unittest

from text_node_split import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
class TestNodeSplitter(unittest.TestCase):
    def test_split1(self):
        old_node = [TextNode("BLACK AND BLUE", text_type_bold),
                    TextNode("Red **all** over", text_type_text)]
        self.assertEqual(
            [TextNode("BLACK AND BLUE", text_type_bold),
             TextNode("Red ", text_type_text),
             TextNode("all", text_type_bold),
             TextNode(" over", text_type_text)],
            split_nodes_delimiter(old_node, "**", text_type_bold)
        )

if __name__ == "__main__":
    unittest.main()