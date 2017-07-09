# level 3
class KthSmallest:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        if k < 1 or k > len(A):
            return -1
        return sorted(A)[k - 1]