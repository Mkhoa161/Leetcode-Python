# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2
            return node1.val == node2.val and is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)

        if not root:
            return False
        queue = [root]
        while queue:
            node = queue.pop(0)
            if is_identical(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
