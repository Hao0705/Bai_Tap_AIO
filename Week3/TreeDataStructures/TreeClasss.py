class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        # Tạo khoảng trắng dựa trên cấp độ của node, mỗi cấp 3 dấu cách
        space = ' ' * (self.get_level() * 3)

        # Nếu node có parent, thêm prefix '|__', nếu không thì không thêm gì
        prefix = space + '|__' if self.parent else ''

        # In dữ liệu của node với prefix
        print(prefix + str(self.data))

        # Nếu node có con, đệ quy in từng con
        if self.children:
            for child in self.children:
                child.print_tree()

def create_tree():
    a_node = TreeNode("A")
    b_node = TreeNode("B")
    c_node = TreeNode("C")
    d_node = TreeNode("D")
    e_node = TreeNode("E")
    f_node = TreeNode("F")
    g_node = TreeNode("G")
    h_node = TreeNode("H")

    a_node.add_children(b_node)
    a_node.add_children(c_node)
    b_node.add_children(d_node)
    b_node.add_children(e_node)
    c_node.add_children(f_node)
    c_node.add_children(g_node)
    c_node.add_children(h_node)

    return a_node

tree = create_tree()
tree.print_tree()
