class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned= ""
        # clean s: remove non-alphanumeric characters and make lowercase
        for c in s:
            if c.isalnum():
                cleaned += c.lower()

        # create a reversed version of the cleaned string
        reverse=cleaned[::-1]
        # compare the cleaned string to its reverse
        return cleaned==reverse
        # return True if equal, otherwise False