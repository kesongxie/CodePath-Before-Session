# level 3
class NumRange:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer

    # [80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]
    # [99, 269]
    # 58


    def numRange(self, A, B, C):
        count = 0
        prevSum = 0
        prevSequence = []
        for idx, num in enumerate(A):
            # check if it's in the Range
            if num > C:
                prevSequence = []
                prevSum = 0
                continue
            # the num by itself form a subsequence [num]
            if num >= B and num <= C:
                count += 1
                if idx == 0:
                    prevSequence.append(num)
                    prevSum += num
                    continue

            # add the num to previous sum
            tempSum = prevSum + num
            if tempSum >= B and tempSum <= C:
                i = 0
                prevSum = tempSum
                while tempSum >= B and i < len(prevSequence):
                    count += 1
                    tempSum -= prevSequence[i]
                    i += 1
                prevSequence.append(num)

            elif tempSum < B:
                prevSequence.append(num)
                prevSum = tempSum
            else:
                # start back tracking
                while tempSum > C:
                    tempSum -= prevSequence[0]
                    prevSequence = prevSequence[1:]

                prevSum = tempSum
                # tempSum is guarantee less than or equals to C at this point
                i = 0
                while tempSum >= B and i < len(prevSequence):
                    count += 1
                    tempSum -= prevSequence[i]
                    i += 1
                prevSequence.append(num)

        return count
