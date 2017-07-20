class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        myMap = {}  # key is the value itself, the value is an array index
        for idx, val in enumerate(A):
            if (B - val) not in myMap:
                # This might override the previosu value
                # use separate chaining to resolve the collison issue
                if val not in myMap:
                    myMap[val] = [idx]
                else:
                    myMap[val] = myMap[val] + [idx]

            else:
                return [myMap[B - val][0] + 1, idx + 1]
        return []