class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""#creating the string to be added to
        for s in strs:#looping through the individual words in the strs dict

            res+=str(len(s))+"#"+s#adding the the string we created,the number of letters in the word, #, the word

        return res#returning the newly created word

    def decode(self, s: str) -> List[str]:  

        res = []#creating the empty list to be added to
        i = 0#initializing the loop variable

        while i < len(s):#looping through the entire length of the word 
            j = i# setting variable for indexing 

            while s[j] != "#":#until s at index j is equal to a # it keeps looping
                j += 1 #incrememnting j until finds #

            length = int(s[i:j])# the length variable is found by taking s at i=0 to current j index which # was founc
            res.append(s[j + 1:j + 1 + length])#append the word from letter after hashtag to the entire length of the word
            i = j + 1 + length # adding to put the index of i after the newly added word

        return res

    

            



        


