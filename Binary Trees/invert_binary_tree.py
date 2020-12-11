########################################################################################
# invert_binary_tree.py
#
# Program showing how to invert a binary tree. Only shows the methods and not the
# relevant classes for creating a binary tree.
########################################################################################


class Solution:
    def invert_tree(self, root):
        if root:
            root.left, root.right = (
                self.invert_tree(root.right),
                self.invert_tree(root.left),
            )
        return root

        # more readable version
        # if root:
        #     left = root.left
        #     right = root.right
        #     root.left = right
        #     root.right = left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root


# input [4,2,7,1,3,None,9]

#      4
#    /   \
#   2     7
#  / \     \
# 1   3     9

# output [4,7,2,9,None,3,1]

#      4
#    /   \
#   7     2
#  /     / \
# 9     3   1