#week10-4.py
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0
        if root.left!=None and root.left.left==None and root.left.right==None:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)