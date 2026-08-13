class Solution:
    def isPalindrome(self, s: str) -> bool:
        sclean=[]

        for i in s:
            if i.isalnum():
                sclean.append(i.lower())

        reversed_text = sclean[::-1]

        if reversed_text==sclean:
            return True
        return False
        


        