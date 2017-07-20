class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):

        # Your Input:
        # 1 2 3 4 5 6 7 8 9
        # k = 2
        # Expected output is 8 -> 9 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

        # find the k to the last element, in this case, 8 as the head
        # k - 1 element as the tail


        # three pointers, one is k step ahead
        # prev = cur - 1, cur, cur + k

        ahead = A
        # walk ahead for k steps first
        count = 0
        while (ahead != None and count < B):
            ahead = ahead.next
            count += 1

        prev = None
        cur = A
        tail = None
        while (ahead != None):
            prev = cur
            cur = cur.next
            if ahead.next == None:
                # ahead is pointing to the tail, then we want to save
                # a reference of the tail for later concatenation
                tail = ahead
            ahead = ahead.next

        prev = None
        tail.next = A

        return cur
