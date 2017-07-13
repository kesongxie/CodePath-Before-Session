class MaxSumContinousSequence:
    # @param A : tuple of integers
    # @return an integer

    # [-2,1,-3,4,-1,2,1,-5,4]    [4,-1,2,1], 6
    def maxSubArray(self, A):
        size = len(A)
        if size == 0:
            return None
        # use two varibales to allow it to explore
        global_max = A[0]
        current_max = A[0]  # the current max
        for i in xrange(1, size):
            current_max = max(A[i], current_max + A[i])
            if current_max > global_max:
                global_max = current_max
        return global_max


