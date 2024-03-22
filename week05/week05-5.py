# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[] #先把a射程很小的,短短的陣列list
        while head != None:
            a.append(head.val)#把head那一串轉換成陣列a
            head = head.next
        

        N = len(a) #a有多少數字
        for i in range(N): #i就照迴圈跑
            if a[i] != a[N-1-i]: return False# 頭尾不相同
        return True#先亂寫