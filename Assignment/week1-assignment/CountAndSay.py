class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        # 1, 11, 21, 1211, 111221, 312211

        # count + actual value
        cur = "1"
        if A == 0:
            return ""
        if A == 1:
            return cur
        curCount = 0
        while (curCount < A - 1):
            temp = ""
            strToIterate = cur  # 1211
            while (len(strToIterate) > 0):
                count = self.countConsecutive(strToIterate[0], strToIterate)
                temp += str(count) + strToIterate[0]
                strToIterate = strToIterate[count:]
            cur = temp
            curCount += 1
        return cur

    def countConsecutive(self, x, cur):
        count = 1
        for i in xrange(1, len(cur)):
            if cur[i] == x:
                count += 1
            else:
                break
        return count





