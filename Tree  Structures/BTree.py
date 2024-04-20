class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, degree):
        self.root = BTreeNode()
        self.degree = degree

    def insert(self, key):
        if len(self.root.keys) == (2 * self.degree) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        index = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1
            node.keys[index + 1] = key
        else:
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == (2 * self.degree) - 1:
                self.split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key)

    def split_child(self, parent, index):
        degree = self.degree
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[degree:(2 * degree) - 1]
        child.keys = child.keys[:degree - 1]
        if not child.leaf:
            new_child.children = child.children[degree:]
            child.children = child.children[:degree]

    def search(self, key):
        return self.search_node(self.root, key)

    def search_node(self, node, key):
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
        if index < len(node.keys) and key == node.keys[index]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search_node(node.children[index], key)

# Example usage:
b_tree = BTree(3)  # Create a B-tree with degree 3
keys = [2, 5, 7, 1, 8, 9, 3, 6, 4]
for key in keys:
    b_tree.insert(key)

print("Search results:")
for key in keys:
    print(key, b_tree.search(key))
