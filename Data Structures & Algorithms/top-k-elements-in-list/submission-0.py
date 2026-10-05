class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        FrequencyCounter = {}

        for number in nums: 
            if number not in FrequencyCounter:
                FrequencyCounter[number] = 1
            else: 
                FrequencyCounter[number]+=1
        
        result=[]
        for index in range(k):
            #resetting the maxKey
            maxKey = None
            maxValue = 0
            for key,v in FrequencyCounter.items():
                if v>maxValue:
                    maxValue=v
                    maxKey=key
            result.append(maxKey)
            #remove the key from the dictionary so it does not get picked again
            del FrequencyCounter[maxKey]
        
        return result




# FrequencyCounter = {
# 1: 1
# 2: 2
# 3: 3



# }

        
