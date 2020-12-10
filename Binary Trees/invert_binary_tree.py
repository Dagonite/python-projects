# invert_binary_tree.py


def invert_tree(self, root):
    if root:
        root.left, root.right = self.invert_tree(root.right), self.invert_tree(
            root.left
        )
    return root


# input [4,2,7]

# invert_tree(root)                # [4,2,7]

#     invert_tree(root.right)      # 7

#         invert_tree(root.right)  # None
#         return root              # None

#         invert_tree(root.left)   # None
#         return root              # None

#     root.left = None
#     root.right = None
#     return root                  # 7

#     invert_tree(root.left)       # 2

#         invert_tree(root.right)  # None
#         return root              # None

#         invert_tree(root.left)   # None
#         return root              # None

#     root.left = None
#     root.right = None
#     return root                  # 2

# root.left = 7
# root.right = 2
# return root                      # [4,7,2]
