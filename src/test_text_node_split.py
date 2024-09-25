import unittest

from textnode_convert import (split_nodes_delimiter,
                              extract_markdown_links,
                              extract_markdown_images,
                              split_nodes_image,
                              split_nodes_link,
                              text_to_textnodes
)
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

class TestNodeLinkExtract(unittest.TestCase):
    def test_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')],
            extract_markdown_links(text)
        )

    def test_image_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertCountEqual(
            [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')],
            extract_markdown_images(text)
        )

class TestNodeLinkSplitter(unittest.TestCase):
    def test_image_split(self):
        nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", text_type_text), TextNode(" and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)]
        self.assertEqual(
            [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")],
            split_nodes_image(nodes)
        )

    def test_image_split2(self):
        nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), ![milk](https://i.imgur.com/HBBhjOP.jpeg)", text_type_text), TextNode(" and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)]
        self.assertEqual(
            [TextNode("This is text with a ", text_type_text), TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"), TextNode(", " , text_type_text, None), TextNode("milk", text_type_image, "https://i.imgur.com/HBBhjOP.jpeg"),TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")],
            split_nodes_image(nodes)
        )
    def test_image_split3(self):
        nodes = [TextNode("This is text", text_type_text), TextNode(" and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)]
        self.assertEqual(
            [TextNode("This is text", text_type_text),TextNode(" and ", text_type_text), TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")],
            split_nodes_image(nodes)
        )

    def test_link_split(self):
        nodes = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text
            )]
        self.assertEqual([TextNode("This is text with a link ", text_type_text), TextNode("to boot dev", text_type_link, "https://www.boot.dev"), TextNode(" and ", text_type_text), TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")],
                         split_nodes_link(nodes))

class TestNodeTexttoTextNode(unittest.TestCase):
    def test_TexttoTN(self):
        example_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
            [TextNode("This is ", text_type_text, None),
             TextNode("text", text_type_bold, None),
             TextNode(" with an ", text_type_text, None),
             TextNode("italic", text_type_italic, None),
             TextNode(" word and a ", text_type_text, None),
             TextNode("code block", text_type_code, None),
             TextNode(" and an ", text_type_text, None),
             TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
             TextNode(" and a ", text_type_text, None),
             TextNode("link", text_type_link, "https://boot.dev")],
             text_to_textnodes(example_text))

if __name__ == "__main__":
    unittest.main()