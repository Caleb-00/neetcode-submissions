class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create hash
        seen = set()

        #loop through the list
        for number in nums:
            #check if number is in the hash already
            if(number in seen):
                return True
            #if not in the hash push to hash 
            else:
                seen.add(number)
#If after looping through everything there is no dup return false
        return False
