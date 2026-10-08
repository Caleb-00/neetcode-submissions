class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #you can use a set split into sections based on if the number below is one less until you find the start 

        numset=set(nums)
        
        longest=0
        
        for n in numset:
            if (n-1) not in numset:
                length=0
                while(n+length) in numset:
                    length+=1
                longest=max(length,longest)

        return longest
