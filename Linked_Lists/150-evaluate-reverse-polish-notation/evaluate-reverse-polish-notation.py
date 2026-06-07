class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expr = ["+","*","/","-"]

        for c in tokens:
            c = c.strip()  # Removes any accidental trailing or leading spaces
            if c in expr:
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                if c == "+":
                    stack.append(t1+t2)
                elif c == "-":
                    stack.append(t2-t1)
                elif c == "*":
                    stack.append(t2*t1)
                elif c == "/":
                    stack.append(int(t2/t1))
            else:
                stack.append(int(c))
        return stack[-1]