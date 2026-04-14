


from blocktoblocktype import block_to_block_type, BlockType
from markdowntoblocks import markdown_to_blocks
from texttochildren import text_to_children
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return create_paragraph_node(block)
    if block_type == BlockType.HEADING:
        return create_heading_node(block)
    if block_type == BlockType.CODE:
        return create_code_node(block)
    if block_type == BlockType.QUOTE:
        return create_quote_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return create_ul_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return create_ol_node(block)
    raise ValueError("Invalid block type")

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def create_ul_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def create_ol_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        # Split by the first dot and space to remove "1. ", "2. ", etc.
        # We find the first index of ". " and slice from after it
        content = line[line.find(". ") + 2:]
        children = text_to_children(content)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def create_code_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        # Strip the > and the leading space if it exists
        new_lines.append(line.lstrip(">").strip())
    
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
