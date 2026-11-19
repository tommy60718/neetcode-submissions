class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize: tokens = ["1","2","+","3","*","4","-"]
        token_stack = []

        #Main loop
        for token in tokens:
            if token == "+":
                token_stack.append(token_stack.pop() + token_stack.pop())
            elif token == "-":
                # second pop - first pop
                a, b = token_stack.pop(), token_stack.pop()
                token_stack.append( b-a )
            elif token == "*":
                token_stack.append(token_stack.pop() * token_stack.pop())
            elif token == "/":
                # second pop / first pop
                a, b = token_stack.pop(), token_stack.pop()
                token_stack.append( int(b/a) )
            else:
                token_stack.append(int(token))
        # Return
        return token_stack.pop()
