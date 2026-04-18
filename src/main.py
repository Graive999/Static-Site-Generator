from generatepage import generate_page
from textnode import TextNode, TextType
from pathlib import Path
import os
import shutil
import sys

default_basepath = "/"

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                dest_html_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_html_path, basepath)
        
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    source_static = "./static"
    dest_public = "./docs"

    print("Deleting public directory...")
    if os.path.exists(dest_public):
        shutil.rmtree(dest_public)

    print("Copying static files to public directory...")
    copy_files_recursive(source_static, dest_public)


    content_dir = "content"
    template = "template.html"
    dest_dir = "docs"

    print(f"Generating pages from {content_dir} to {dest_dir} using {template}...")
    generate_pages_recursive(content_dir, template, dest_dir, basepath)

if __name__ == "__main__":
    main()