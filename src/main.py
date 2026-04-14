from generatepage import generate_page
from textnode import TextNode, TextType
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

def main():
    source_static = "./static"
    dest_public = "./public"

    print("Deleting public directory...")
    if os.path.exists(dest_public):
        shutil.rmtree(dest_public)

    print("Copying static files to public directory...")
    copy_files_recursive(source_static, dest_public)


    generate_page(
        "content/index.md", 
        "template.html", 
        "public/index.html"
    )

if __name__ == "__main__":
    main()