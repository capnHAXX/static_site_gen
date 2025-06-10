import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def text_to_textnodes(text):
    new_nodes = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "_", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown, check delimiters")
        split_nodes = []
        for i in range(0,len(split_text)):
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    extractor = []
    extractor = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return extractor

def extract_markdown_links(text):
    extractor = []
    extractor = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return extractor

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        image_markdown = extract_markdown_images(original_text)
        if len(image_markdown) == 0:
            new_nodes.append(old_node)
            continue
        for m in image_markdown:
            alt_text = m[0]
            hyperlink = m[1]
            sections = original_text.split(f"![{alt_text}]({hyperlink})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid image markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(alt_text, text_type_image, hyperlink))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        link_markdown = extract_markdown_links(original_text)
        if len(link_markdown) == 0:
            new_nodes.append(old_node)
            continue
        for l in link_markdown:
            link_text = l[0]
            hyperlink = l[1]
            sections = original_text.split(f"[{link_text}]({hyperlink})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid link markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link_text, text_type_link, hyperlink))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
        