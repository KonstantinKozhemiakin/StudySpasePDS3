class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return False
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return False
            return self.right.findval(find_val)
        else:
            return Tree

    def add_elements(self, list_of_node):
        for node in list_of_node:
            if node is None:
                continue
            self.insert(node)

    def find_min(self):
        if self.left == None:
            return self.id_node
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right == None:
            return self.id_node
        else:
            return self.right.find_max()

    def delete_node(self, node):
        if self.findval(node):
            if self.id_node is None:
                return self.id_node
            if node < self.id_node:
                self.left = self.left.delete_node(node)
            elif node > self.id_node:
                self.right = self.right.delete_node(node)
            else:
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                elif self.right is None:
                    temp = self.left
                    self = None
                    return temp
                temp = self.right.find_min()
                self.id_node = temp
                self.right = self.right.delete_node(temp)
            return self

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()


# tr = Tree(5)
# nodes = [8, 3, 15, 1, 6, 14, None,  7, None, None, 13, 49, 16, 17, 46, 18, 19]
# tr.add_elements(nodes)
# tr.print_tree()
# tr.delete_node(13)
# tr.print_tree()
