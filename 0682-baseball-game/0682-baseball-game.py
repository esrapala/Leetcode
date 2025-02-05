class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        # This is O(N) since we are iterating through
        # Since we are using lifo, stack is great but we can implement it with list as in this example
        
        stack = []
        
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        
        return sum(stack)