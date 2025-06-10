import os
import shutil
import sys
from website_builder import (copy_files_recursive, generate_pages_recursive)
public_path = "./docs"
static_path = "./static"
template_path = "./template.html"
content_path = "./content"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)

    print("copying files")
    copy_files_recursive(static_path, public_path)

    generate_pages_recursive(content_path, template_path, public_path, basepath)

main()