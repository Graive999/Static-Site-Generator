import os
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    
    
    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()
    
    
    title = extract_title(markdown_content)
    
    
    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
        
    
    with open(dest_path, 'w') as f:
        f.write(full_html)