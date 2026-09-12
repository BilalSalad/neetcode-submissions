from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        result = []

        for num in nums:
            map[num] += 1
        
        
        for i in range(k):
            max_num = max(map, key = map.get)
            result.append(max_num)
            map.pop(max_num)

        return result

