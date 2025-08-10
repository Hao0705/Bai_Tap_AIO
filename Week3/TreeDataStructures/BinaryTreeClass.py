from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):

        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        q = deque([self.root])

        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                q.append(node.right)

    def find(self, value):
        if not self.root:
            return None

        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.data == value:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.left)

        return None

    def remove(self, value):
        if not self.root:
            return

        q = deque([self.root])
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while q:
            last_node = q.popleft()

            if last_node.data == value:
                node_to_delete = last_node
            if last_node.left:
                parent_of_last = last_node
                q.append(last_node.left)
            if last_node.right:
                parent_of_last = last_node
                q.append(last_node.right)

        if node_to_delete:
            node_to_delete.data = last_node.data
            if parent_of_last.left == last_node:
                parent_of_last.left = None
            if parent_of_last.right == last_node:
                parent_of_last.right = None

    def depth_node(self, target_node):
        if not self.root or not target_node:
            return -1

        q = deque([(self.root, 0)])
        while q:
            node, d = q.popleft()
            if node == target_node:
                return d
            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))

        return -1

    # Tính độ cao của cây
    def height(self):
        def calc_height(node):
            if not node:
                return -1
            return 1 + max(calc_height(node.left), calc_height(node.right))

        return calc_height(self.root)

    # In cây dạng duyệt level
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

print("=== Binary Tree ===")
bt = BinaryTree()
bt.add(10)
bt.add(5)
bt.add(15)
bt.add(3)
bt.add(7)
bt.add(20)
bt.add(25)
bt.remove(10)
bt.print_tree()
