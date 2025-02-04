class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1_map = {}

        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        
        for i in range(len(s2) - len(s1) + 1):
            w_map = {}

            if s2[i] in s1_map:

                for j in range(i, i + len(s1)):
                    w_map[s2[j]] = 1 + w_map.get(s2[j], 0)

                if w_map == s1_map: return True
        
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: 
            return False
        
        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(n1): # build the frequency map for the first window
            s1_map[ord(s1[i]) - 97] += 1 
            s2_map[ord(s2[i]) - 97] += 1
        
        # compare the frequency maps of the first window
        if s1_map == s2_map: return True

        # slide the window and compare the frequency maps
        # the window starts from n1 as we already compared the first window
        # we slide the window to the right by 1 and compare the frequency maps
        for i in range(n1, n2):
            s2_map[ord(s2[i]) - 97] += 1 
            s2_map[ord(s2[i - n1]) - 97] -= 1
            if s1_map == s2_map: 
                return True
        
        return False

