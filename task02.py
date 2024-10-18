class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def find_min(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.value

bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)
bst.insert(11)
bst.insert(16)
bst.insert(4)
bst.insert(51)
bst.insert(2)
bst.insert(13)


min_value = bst.find_min()
print("Найменше значення в дереві:", min_value)