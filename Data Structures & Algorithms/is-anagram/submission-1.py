class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else: 
            dict_a={}
            dict_b={}

            # placing each char of the string into the dict, and get it's count/freq.
            for char in s: 
                dict_a[char]=dict_a.get(char,0)+1
            
            for char in t:
                dict_b[char]=dict_b.get(char,0)+1

            
            # checking the dictionary to see if they are equal in frequency.

            if dict_a == dict_b:
                return True
            else: 
                return False


