# level 2

# input:
# A = 4
#
# output:
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

class PrettyPrint:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2 * A - 1
        arr = [[0] * size for _ in range(size)]
        edge_1 = 0
        edge_2 = size - 1
        for i in xrange(size):
            for j in xrange(size):
                # calculate the min distance to the edge, which is 0, (size - 1)
                dis_1 = abs(i - edge_1)
                dis_2 = abs(i - edge_2)
                dis_3 = abs(j - edge_1)
                dis_4 = abs(j - edge_2)
                minDis = min(dis_1, dis_2, dis_3, dis_4)
                arr[i][j] = A - minDis
        return arr