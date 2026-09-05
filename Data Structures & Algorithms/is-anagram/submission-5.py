class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else: 
            dict1 = {}
            dict2={}
            
        for item in s:
            if item in dict1:
                dict1[item]+=1
            else:
                dict1[item]=1
        
        #second string
        for item in t:
            if item in dict2:
                dict2[item]+=1
            else:
                dict2[item]=1
        return dict2==dict1
            