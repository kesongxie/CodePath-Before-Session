class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        hStackLen = len(haystack)
        nLen = len(needle)
        if hStackLen == 0 or nLen == 0:
            return -1
        for i in xrange(hStackLen - nLen + 1):
            h_index = i
            n_index = 0
            for n in needle:
                if n != haystack[h_index]:
                    break
                else:
                    h_index += 1
                    n_index += 1
            if n_index == nLen:
                return i
        return -1








