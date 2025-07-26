def is_pallindrome(st):
    return st == st[::-1]


def dfs(start_i, path, res, n, s):

    # end case
    if start_i == n:
        #print(path)
        res.append(path.copy())
        #print(res)
        return

    # get edges
    for end in range(start_i, n):
        chunk = s[start_i:end+1]
        if is_pallindrome(chunk):
            path.append(chunk)
            dfs(end+1, path, res, n, s)
            #print(res)
            path.pop()
    



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        if s:
            dfs(0, path, res, n, s)
        #print(res)
        return res
        