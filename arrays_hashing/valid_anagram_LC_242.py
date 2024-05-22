class Solution:
    # Solution 1
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        counter_dict = {}

        for i in range(len(s)):
            if s[i] not in counter_dict:
                counter_dict[s[i]] = 1
            else:
                counter_dict[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in counter_dict:
                return False
            counter_dict[t[j]] -= 1

        for values in counter_dict.values():
            if values!=0:
                return False

        return True 
    
class Solution:
    # Solution 2
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        
        return counter_s == counter_t
            
        