from collections import deque
from idlelib.debugobj_r import remote_object_tree_item


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        def insert(node, data):

            if not node:
                return Node(data)
            if data < node.data:
                node.left = insert(node.left, data)
            else:
                node.right = insert(node.right, data)

            return node
        self.root = insert(self.root, data)

    def find(self, data):
        def search(node, data):
            if not node or node.data == data:
                return node
            if node.data < data:
                return search(node.right, data)
            else:
                return search(node.left, data)

        return search(self.root, data)

    def remove(self, data):
        def delete(node, data):
            if not node:
                return node
            if data < node.data:
                node.left = delete(node.left, data)
            elif data > node.data:
                node.right = delete(node.right, data)
            else:
                # Node lá
                if not node.left and not node.right:
                    return None
                # Node có 1 con
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Node có 2 con
                successor = self.min_value_node(node.right)
                node.data = successor.data
                node.right = delete(node.right, successor.data)
            return node

        self.root = delete(self.root, data)

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_tree(self):
        if not self.root:
            print("Cây rỗng")
            return

        q = deque([(self.root, 0)])
        current_level = 0
        line = ""
        while q:
            node, level = q.popleft()
            if level != current_level:
                print(line)
                line = ""
                current_level = level
            line += str(node.data) + " "
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        print(line)

print("\n=== Binary Search Tree ===")
bst = BinarySearchTree()
bst.add_node(10)
bst.add_node(5)
bst.add_node(15)
bst.add_node(3)
bst.add_node(7)
bst.print_tree()

bst.remove(5)
print("BST sau khi xóa 5:")
bst.print_tree()

