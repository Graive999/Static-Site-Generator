import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "Click me!", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode("div", "Hello World")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode("p", "sample text")
        self.assertEqual(
            repr(node), 
            "HTMLNode(p, sample text, children: None, None)"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(node.to_html()) 


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

if __name__ == "__main__":
    unittest.main()