class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)
        result = []

        for num in nums:
            num_map[num] += 1
            
        
        for i in range(k):
            max_num = max(num_map, key = num_map.get)
            result.append(max_num)
            num_map.pop(max_num)
        
        return result