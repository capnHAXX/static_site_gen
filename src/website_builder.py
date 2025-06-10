import shutil
import os
from pathlib import Path
from block_handling import (markdown_to_blocks, block_to_block_type,
                            block_type_heading, markdown_to_html_node)

def copy_files_recursive(source_directory_path, dest_directory_path):
    print(f"copying files from {source_directory_path} to {dest_directory_path}")
    if not os.path.exists(dest_directory_path):
        os.mkdir(dest_directory_path)
    
    for file in os.listdir(source_directory_path):
        from_path = os.path.join(source_directory_path,file)
        destination_path = os.path.join(dest_directory_path,file)
        if os.path.isfile(from_path):
            shutil.copy(from_path, destination_path)
        else:
            copy_files_recursive(from_path, destination_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            split_header = block.split()
            hash_count = len(split_header[0])
            if hash_count == 1:
                title = " ".join(split_header[1:])
                return title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    page_html = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    new_template = template.replace("{{ Title }}", page_title).replace("{{ Content }}", page_html).replace('href="/', 'href="' + basepath).replace('src="/', 'src="' + basepath)

    os.mknod(dest_path)
    with open(dest_path, "w") as f:
        f.write(new_template)
        f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content,file)
        new_dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            if from_path.split(".")[-1] == "md":
                new_dest_path = new_dest_path.replace(".md",".html")
                generate_page(from_path, template_path, new_dest_path, basepath)
        
        else:
            generate_pages_recursive(from_path, template_path, new_dest_path, basepath)

