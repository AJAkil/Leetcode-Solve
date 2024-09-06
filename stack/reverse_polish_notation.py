class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                
                b = s.pop()
                a = s.pop()
                
                if t == '+':
                    s.append(a+b)
                elif t == '-':
                    s.append(a-b)
                elif t == '*':
                    s.append(a*b)
                elif t == '/':
                    s.append(int(a/b))

            else:
                s.append(int(t))
            
        return s.pop()
        