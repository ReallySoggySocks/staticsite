from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_list = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
        else:
            new_nodes = node.text.split(delimiter)
            if len(new_nodes) % 2 != 0:
                raise Exception("Unevern Delimiter - Invalid Markdown Syntax")

            for i, text in enumerate(new_nodes):
                if not text.strip():
                    continue

                if i %2 == 0:
                    new_list.append(TextNode(text, TextType.TEXT))
                else:
                    new_list.append(TextNode(text, text_type))

    return new_list