class PascalTriangle:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        results = [[1]]

        # [  [1],   [1, 1] ]
        for i in xrange(1, A):
            results.append([])
            for j in xrange(i + 1):
                prev_1 = 0
                if j < len(results[i - 1]):
                    prev_1 = results[i - 1][j]
                prev_2 = 0
                if j - 1 > -1:
                    prev_2 = results[i - 1][j - 1]
                results[i].append(prev_1 + prev_2)
        return results