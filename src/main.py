import os
import shutil
from website_builder import (copy_files_recursive, generate_pages_recursive)
public_path = "./public"
static_path = "./static"
template_path = "./template.html"
content_path = "./content"

def main():
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)

    print("copying files")
    copy_files_recursive(static_path, public_path)

    generate_pages_recursive(content_path, template_path, public_path)

main()