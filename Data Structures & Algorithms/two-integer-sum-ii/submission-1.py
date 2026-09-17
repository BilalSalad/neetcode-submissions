class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_map = {}
        r = len(numbers) - 1
        l = 0

        for num in numbers:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total == target:
                return [l + 1, r + 1]
            else:
                l += 1
            
        return []

            
