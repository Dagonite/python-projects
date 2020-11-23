# flatten_binary_tree_to_linked_list.py

def flatten(self, root):
    self.previous_right = None

    def helper(root=root):
        if root:
            helper(root.right)
            helper(root.left)
            root.right, self.previous_right = self.previous_right, root
            root.left = None

    helper()
