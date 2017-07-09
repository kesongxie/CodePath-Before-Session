#Level 5
class AllUniquePermutation:
    # @param A : list of integers
    # @return a list of list of integers
    # [1,1,2] -> [ [1,1,2], [1,2,1], [2,1,1] ]
    # [1, 2, 3] -> [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    def permute(self, A):
        results = [[]]
        for n in A:
            temp_result = []
            temp_set = set()
            for l in results:
                for i in xrange(len(l) + 1):
                    s = l[:i] + [n] + l[i:]
                    str_s = self.stringifyList(s)
                    if str_s not in temp_set:
                        temp_set.add(str_s)
                        temp_result.append(s)
                        results = temp_result
        return results

    # returns a string representation of a list
    def stringifyList(self, A):
        h = ""
        for e in A:
            h += str(e) + ":"
        return h