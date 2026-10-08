class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned=""#empty string

        for l in s:#looping through the old string
            if l.isalnum():#if it is a character
                cleaned+=l.lower()#add the letter and make it lowercase



        reverse=cleaned[::-1]#reverse the list and place it into reverse variable


        return cleaned==reverse#return true or false based on if reverse and string cleaned match