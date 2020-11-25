# binary_tree_dfs_traversals.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, traversal_type=""):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")

        else:
            print("Traversal type", str(traversal_type), "is not supported")
            return False

    def preorder(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += str(start.val) + " "
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.val) + " "
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.val) + " "
        return traversal


tree1 = BinaryTree("A")
tree1.root.left = TreeNode("B")
tree1.root.right = TreeNode("C")
tree1.root.left.left = TreeNode("D")
tree1.root.left.right = TreeNode("E")
tree1.root.right.left = TreeNode("F")
tree1.root.right.right = TreeNode("G")
#                A
#             /    \
#            B      C
#           / \    / \
#          D  E   F  G

tree2 = BinaryTree(1)
tree2.root.left = TreeNode(2)
tree2.root.right = TreeNode(3)
tree2.root.left.left = TreeNode(4)
tree2.root.left.right = TreeNode(5)
tree2.root.right.right = TreeNode(6)
tree2.root.left.left.left = TreeNode(7)
tree2.root.left.left.right = TreeNode(8)
tree2.root.right.right.left = TreeNode(9)
#                1
#             /    \
#            2      3
#           / \      \
#          4  5       6
#         / \        /
#        7  8       9

print("Preorder traversal: {:>16}".format(tree1.print_tree("preorder")))
print("Inorder traversal: {:>17}".format(tree1.print_tree("inorder")))
print("Postorder traversal: {:>15}".format(tree1.print_tree("postorder")))
print()
print("Preorder traversal: {:>20}".format(tree2.print_tree("preorder")))
print("Inorder traversal: {:>21}".format(tree2.print_tree("inorder")))
print("Postorder traversal: {:>19}".format(tree2.print_tree("postorder")))
