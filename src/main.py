from generatepage import generate_page
from textnode import TextNode, TextType
from pathlib import Path
import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            # If it's a directory, recurse!
            copy_files_recursive(from_path, dest_path)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Iterate over every entry in the content directory
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        # If it's a file, check if it's markdown and generate HTML
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                # Change extension from .md to .html
                dest_html_path = Path(dest_path).with_suffix(".html")
                # Use your existing generate_page function
                generate_page(from_path, template_path, dest_html_path)
        
        # If it's a directory, create it in public and recurse
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)

def main():
    source_static = "./static"
    dest_public = "./public"

    print("Deleting public directory...")
    if os.path.exists(dest_public):
        shutil.rmtree(dest_public)

    print("Copying static files to public directory...")
    copy_files_recursive(source_static, dest_public)


    content_dir = "content"
    template = "template.html"
    dest_dir = "public"

    print(f"Generating pages from {content_dir} to {dest_dir} using {template}...")
    generate_pages_recursive(content_dir, template, dest_dir)

if __name__ == "__main__":
    main()