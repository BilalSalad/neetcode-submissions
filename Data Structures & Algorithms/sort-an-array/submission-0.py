class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                j += 1
            i += 1
        
        return nums
