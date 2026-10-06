class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
            
        num_frequency={}

        for number in nums:
            if number not in num_frequency:
                num_frequency[number]=1
            else:
                num_frequency[number]+=1
        
        # go over each key and value
        result = []
        for index in range(k):
            maxValue = 0
            maxKey = None
            for key,value in num_frequency.items():
                if value > maxValue:
                    maxValue=value
                    maxKey=key        
            result.append(maxKey)
            del num_frequency[maxKey]
        return result





#  num_frequency           {
# 1:1 
# 2:2
# 3:3




#             }

