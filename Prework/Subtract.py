# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#level 4

class Subtract:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        # split the linked-list into two from the middle
        # using two pointers to split the linked-list

        if A == None:
            return A

        if A.next == None:
            return A

        # at this point, we guarantee to have at least two nodes in the list
        ptr_1 = A
        ptr_2 = A  # the ptr that is two step ahead

        while ptr_2 != None:
            # ptr_2 attempts to traval two steps ahead
            if ptr_2.next != None and ptr_2.next.next != None:
                ptr_2 = ptr_2.next.next
                ptr_1 = ptr_1.next
            else:
                break

        # remember the mid point for later merging two linked-list together
        mid_point = ptr_1
        # the head of the second half of the linked-list
        head_second = ptr_1.next

        # reverse the second half of the linked list
        head_second_reversed = self.reverse(head_second)

        ptr_3 = A
        ptr_4 = head_second_reversed

        # do the subtraction
        while ptr_4 != None:
            ptr_3.val = ptr_4.val - ptr_3.val
            ptr_4 = ptr_4.next
            ptr_3 = ptr_3.next

        head_second_normal = self.reverse(head_second_reversed)

        # merge the linked list together
        mid_point.next = head_second_normal

        return A

    # @param A : head node of linked list
    # @return the head node in the reversed linked list
    def reverse(self, A):
        # 4 -> 5 -> 6
        prev = None
        cur = A
        temp = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev







