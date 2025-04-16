# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inorder(root, arr)
        return arr[k-1]
    
    def inorder(self, node: Optional[TreeNode], arr: [int]) -> None:
        if node is None:
            return
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
        
