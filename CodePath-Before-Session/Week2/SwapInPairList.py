# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        # 1->2->3->4->5
        # 
        prev = None
        cur = A
        if cur != None and cur.next != None:
            A = cur.next

        while cur != None and cur.next != None:
            temp = cur.next.next
            if prev != None:
                prev.next = cur.next
            cur.next.next = cur
            cur.next = temp
            prev = cur
            cur = temp
        return A
