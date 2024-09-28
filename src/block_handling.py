block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unorder_list = "unordered list"
block_type_order_list = "ordered list"

from textnode_convert import text_to_textnodes
from textnode import TextNode
from htmlnode import (HTMLNode, ParentNode)

def markdown_to_blocks(markdown):
    new_markdown = markdown
    blocks = new_markdown.split("\n\n")
    block_list = []
    for b in blocks:
        b = b.strip()
        if len(b) != 0:
            block_list.append(b)
    return block_list

def block_to_block_type(block):
    split_block = block.split("\n")
    if block.startswith("#"):
        hash_string = block.split()[0]
        hash_count = len(hash_string)
        if hash_count >= 1 and hash_count <= 6:
            return block_type_heading
        return block_type_paragraph
    elif block.startswith("```") and block.endswith("```") and len(block) > 6:
        if len(split_block) > 2:
            return block_type_code
        return block_type_paragraph
    elif all(line.startswith(">") for line in split_block):
        return block_type_quote
    elif all(line.startswith("* ") or line.startswith("- ") for line in split_block):
        return block_type_unorder_list
    elif all(line.startswith(f"{i+1}. ") for i, line in enumerate(split_block)):
        return block_type_order_list
    else:
        return block_type_paragraph
    
def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    children = []
    for block in block_list:
        converted_block = block_converter(block)
        children.append(converted_block)
    return ParentNode("div", children, None)


def block_converter(block):
    block_type = block_to_block_type(block)
    html_node = ""
    if block_type == block_type_paragraph:
        html_node = paragraph_block_convert(block)
    elif block_type == block_type_heading:
        html_node = heading_block_convert(block)
    elif block_type == block_type_code:
        html_node = code_block_convert(block)
    elif block_type == block_type_quote:
        html_node = quote_block_convert(block)
    elif block_type == block_type_unorder_list:
        html_node = ul_block_convert(block)
    elif block_type == block_type_order_list:
        html_node = ol_block_convert(block)
    return html_node

def text_to_children(block):
    leaf_nodes = []
    text_nodes = text_to_textnodes(block)
    for node in text_nodes:
        leaf_node = node.text_to_leaf()
        leaf_nodes.append(leaf_node)
    return leaf_nodes

def paragraph_block_convert(block):
    split_block = block.split("\n")
    paragraph = " ".join(split_block)
    return ParentNode("p",text_to_children(paragraph))

def heading_block_convert(block):
    hash_count = len(block.split()[0])
    new_block = " ".join(block.split()[1:])
    return ParentNode(f"h{hash_count}",text_to_children(new_block))

def code_block_convert(block):
    new_block = block.replace("```", "")
    children = text_to_children(new_block)
    code_block = ParentNode("code", children)
    return ParentNode("pre", [code_block])

def quote_block_convert(block):
    split_block = block.split("\n")
    lines = []
    for sub_block in split_block:
        new_line = sub_block.lstrip(">").strip()
        lines.append(new_line)
    new_block = " ".join(lines)
    return ParentNode("blockquote",text_to_children(new_block))

def ul_block_convert(block):
    split_block = block.split("\n")
    lines = []
    for sub_block in split_block:
        if sub_block.startswith("* "):
            stripped_block = sub_block.lstrip("* ")        
        elif sub_block.startswith("- "):
            stripped_block = sub_block.lstrip("- ") 
        sub_node = ParentNode("li",text_to_children(stripped_block))
        lines.append(sub_node)
    return ParentNode("ul",lines)

def ol_block_convert(block):
    split_node = []
    lines = block.split("\n")
    for line in lines:
        new_line = " ".join(line.split(" ")[1:])
        line_node = ParentNode("li",text_to_children(new_line))
        split_node.append(line_node)
    return ParentNode("ol",split_node)
