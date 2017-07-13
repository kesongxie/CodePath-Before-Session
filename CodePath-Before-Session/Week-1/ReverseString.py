class ReverseString:
    # @param A : string
    # @return string

    # the sky is blue

    def reverseWords(self, A):
        str = self.reverse(A)
        words = str.split(" ")
        result = ""
        for w in words:
            result = result + self.reverse(w) + " "
        return result.strip()

    def reverse(self, A):
        reverse = ""
        for c in A:
            reverse = c + reverse
        return reverse