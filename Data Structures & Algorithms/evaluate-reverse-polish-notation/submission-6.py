class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize
        # Stack using a list a container
        store_stack = []
        
        for token in tokens:
            if token == "+":
                store_stack.append(store_stack.pop() + store_stack.pop())
            elif token == "-":
                # second pop - first pop
                a, b = store_stack.pop(), store_stack.pop()
                store_stack.append(int(b - a))
            elif token == "*":
                store_stack.append(store_stack.pop()* store_stack.pop())
            elif token == "/":
                # second pop / first pop(
                a, b = store_stack.pop(), store_stack.pop()
                store_stack.append(int(b/a))
            else:
                store_stack.append(int(token))
        # Always valid input -> Directly output result.
        return store_stack.pop()
