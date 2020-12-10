########################################################################################
# flatten_binary_tree_to_linked_list.py
#
# Program showing how to flatten a binary tree to a linked list. Only shows the methods
# and not the relevant classes for creating a binary tree.
########################################################################################


def flatten(self, root):
    self.previous_right = None

    def helper(root=root):
        if root:
            helper(root.right)
            helper(root.left)
            root.right, self.previous_right = self.previous_right, root
            root.left = None

    helper()
