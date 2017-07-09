# level 4
class Nextgreater:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        for i in xrange(len(A)):
            A[i] = self.findNextGreater(i, A)
        return A

    # @param i : the index of the current num
    # @param A : list of integers
    # @return the next element that in the list that is greater than the current num
    def findNextGreater(self, i, A):
        for j in xrange(i + 1, len(A)):
            if A[j] > A[i]:
                return A[j]
        return -1