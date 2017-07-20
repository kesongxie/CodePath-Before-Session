class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        n = len(A)
        if n == 0:
            return []
        sumDict = dict()
        ret = []
        for i in range(n):
            for j in range(i + 1, n):
                temp = A[i] + A[j]
                if temp in sumDict:
                    sumDict[temp] += [i, j]
                else:
                    sumDict[temp] = [i, j]

        for i in range(n):
            for j in range(i + 1, n):
                # print i, j
                temp = A[i] + A[j]
                if temp in sumDict:
                    tempLst = sumDict[temp]
                    # print temp, tempLst
                    if len(tempLst) >= 4:
                        ret += tempLst[0:2]
                        for k in range(2, len(tempLst), 2):
                            if tempLst[k] > ret[0] and tempLst[k] != ret[1] and tempLst[k + 1] != ret[1]:
                                ret += tempLst[k:k + 2]
                                return ret
                        if len(ret) < 4:
                            ret = []
        if len(ret) < 4:
            ret = []
        return ret