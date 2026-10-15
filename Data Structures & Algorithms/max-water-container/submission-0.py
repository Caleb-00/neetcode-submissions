class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l=0
        r=len(heights)-1

        while l<r:

            width=r-l
            height=min(heights[l],heights[r])
            area=width*height

            res=max(res,area)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1


        return res
            