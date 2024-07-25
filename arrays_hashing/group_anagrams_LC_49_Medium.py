class Solution:

    def is_anagram(s, t):
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_list = []
        is_grouped_set = set()

        for i in range(len(strs)-1):
            temp_list = []
            if strs[i] not in is_grouped_set:
                temp_list.append(strs[i])
                is_grouped_set.add(strs[i])

                for j in range(i+1, len(strs)):
                    print(strs[i], strs[j])
                    if len(strs[j]) == len(strs[i]):
                        if is_anagram(strs[i], strs[j]):
                            temp_list.append(strs[j])
                            is_grouped_set.add(strs[j])
                result_list.append(temp_list)
        
        if strs[len(strs)-1] not in is_grouped_set:
            result_list.append([strs[len(strs)-1]])

        return result_list

# solution 2

import collections 
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = collections.defaultdict(list)

        for s in strs:
            counter = [0] * 26       
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            result_dict[tuple(counter)].append(s)
        
        return result_dict.values()

                    

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat", "eat","tea","tan","ate","nat","bat"]))