class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "]" : "[", "}" : "{"}
        stack = []

        # s = "([{}])"
        for c in s:
            if c in closeToOpen.keys():
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
            else:
                stack.append(c)
        
        return stack == []
