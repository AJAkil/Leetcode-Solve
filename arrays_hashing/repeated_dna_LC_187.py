class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna_patt = {}
        res = []

        for i in range(len(s) - 9):
            current = s[i:i+10]
            dna_patt[current] = 1 + dna_patt.get(current, 0)
        
        for patt, freq in dna_patt.items():
            if freq > 1:
                res.append(patt)
        
        return res

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna_patt = set()
        res = set()

        for i in range(len(s) - 9):
            current = s[i:i+10]
            if current in dna_patt:
                res.add(current)
            
            dna_patt.add(current)
        
        
        return list(res)
        