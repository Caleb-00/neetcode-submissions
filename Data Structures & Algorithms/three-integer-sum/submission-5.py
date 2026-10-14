class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        res=[]#result array

        for i, a in enumerate(nums):# looping through for index and number
            if i >0 and a ==nums[i-1]:#if already used the number cant use again
                continue

            l=i+1#intializing l
            r=len(nums)-1#intializing r
            while l<r:#infinite loop

                sum=a+nums[l]+nums[r]#sum of 3 pointers

                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:#if 3 pointers ==0
                    res.append([a, nums[l], nums[r]])#append them
                    l+=1#increase l,others should be automatic
                    r-=1
                    while  l<r and nums[l]==nums[l-1]:
                        l+=1
                
                
            
        return res    
