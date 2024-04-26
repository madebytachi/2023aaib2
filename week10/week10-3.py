#week10-3.py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0 # 簡單的結束條件
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1