# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        while stack:
            node = stack.pop()
            if (p.val >= node.val and q.val <= node.val) or (p.val <= node.val and q.val >= node.val):
                return node
            
            if p.val <= node.val and q.val <= node.val:
                stack.append(node.left)
            elif p.val >= node.val and q.val >= node.val:
                stack.append(node.right)
        
