#Level 5
class LongestConsecutiveSequence:
    # @param A : tuple of integers
    # @return an integer
    # input: [100, 3, 200, 1, 4, 2]
    # output: 4, [1, 2, 3, 4]
    def longestConsecutive(self, A):
        # make a set out of the given array to remove duplicates
        ans = 0
        mySet = set(A)
        for num in mySet:
            prev = num - 1
            if prev not in mySet:
                # the num is the starting of the sequence
                nxt = num + 1
                while nxt in mySet:
                    nxt += 1
                ans = max(ans, nxt - num)
        return ans

