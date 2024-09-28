import os
import shutil
from website_builder import (copy_files_recursive, generate_page)
public_path = "./public"
static_path = "./static"
template_path = "./template.html"
index_path = "./content/index.md"
index_destination = os.path.join(public_path,"index.html")

def main():
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)

    print("copying files")
    copy_files_recursive(static_path, public_path)

    generate_page(index_path, template_path, index_destination)

main()