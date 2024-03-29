# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        
        def dfs(root):
            if root.left:
                dfs(root.left)

            result.append(root.val)

            if root.right:
                dfs(root.right)
        
        dfs(root)
        return result

            
