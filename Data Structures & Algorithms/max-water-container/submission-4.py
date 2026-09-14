class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = (r - l) * min(heights[l], heights[r])

        while l < r:
           # print("l:", l)
           # print("r:", r)
           # print("heights: ", heights[l], heights[r])

            area = (r - l) * min(heights[l], heights[r])

            if area > max_area:
                max_area = area

           # print("max area: ", max_area)

            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
            
                

        return max_area

