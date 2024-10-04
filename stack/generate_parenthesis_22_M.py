class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []


        def backtrack(o, c):

            if o == c == 0:
                res.append("".join(stack))
                return 
            
            if o > 0:
                stack.append('(')
                backtrack(o-1, c)
                stack.pop()
            
            if c > o:
                stack.append(')')
                backtrack(o, c-1)
                stack.pop()
        
        backtrack(n,n)

        return res
            
        