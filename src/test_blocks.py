import unittest
from block_handling import *

class TestBlockSplitter(unittest.TestCase):
    def test_block_split(self):
        markdown = "# This is a heading \n\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        split_list = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                      "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(split_list, markdown_to_blocks(markdown))
    
    def test_block_blank(self):
        markdown = ""
        split_list = []
        self.assertEqual(split_list, markdown_to_blocks(markdown))

class TestBlocktoBlockType(unittest.TestCase):
    def test_bt1(self):
        block_1 = "##### Welcome"
        self.assertEqual("heading", block_to_block_type(block_1)) #heading

    def test_bt2(self):
        block_2 = "```\nhere my code\n```"
        self.assertEqual("code", block_to_block_type(block_2)) #code

    def test_bt3(self):
        block_3 = "> quote 1\n> quote 2\n not a quote"
        self.assertEqual("paragraph", block_to_block_type(block_3)) #paragraph

    def test_bt4(self):
        block_4 = "> quote 1\n> quote 2\n> quote 3"
        self.assertEqual("quote", block_to_block_type(block_4)) #quote
    
    def test_bt5(self):
        block_5 = "1. fdfafdsa\n2. adsfafdadsf\n3. dfsasdfasdf"
        self.assertEqual("ordered list", block_to_block_type(block_5))

    def test_bt6(self):
        block_6 = "```\ncode```"
        self.assertEqual("paragraph", block_to_block_type(block_6)) #paragraph
    
    def test_bt7(self):
        block_7 = "- fdfafdsa\n- adsfafdadsf\n- dfsasdfasdf"
        self.assertEqual("unordered list", block_to_block_type(block_7)) #paragraph

class TestMDtoHTMLNode(unittest.TestCase):
    def test_mdhtml1(self):
        markdown = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        markdown_to_html = markdown_to_html_node(markdown)
        html_node = markdown_to_html.to_html()
        result = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        self.assertEqual(html_node, result)