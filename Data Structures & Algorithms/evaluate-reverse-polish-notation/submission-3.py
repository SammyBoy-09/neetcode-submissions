class Solution:
    def evalexp(self, n1, n2, op):
        match op:
            case "+":
                return n1 + n2
            case "-":
                return n1 - n2
            case "*":
                return n1 * n2
            case "/":
                return int(n1 / n2)


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for s in tokens:
            if s in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.evalexp(b, a, s))
            else:
                stack.append(int(s))
            
        return stack[0]