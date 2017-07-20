class Solution:
    # @param A : tuple of integers
    # @return an integer

    # [8, 3, 5, 4, 2, 6, 6, 1, 0]

    def maximumGap(self, A):
        if len(A) < 1:
            return -1
        tuples = []
        for idx, ele in enumerate(A):
            tuples.append((ele, idx))

        # sort the tuple based on the key
        sortedTuples = sorted(tuples, key=lambda tup: tup[0])

        mx = 0
        maxJ = {}
        for i in xrange(len(sortedTuples) - 1, -1, -1):
            mx = max(sortedTuples[i][1], mx)
            maxJ[i] = mx

        result = 0
        for i, tu in enumerate(sortedTuples):
            result = max(maxJ[i] - tu[1], result)

        return result


