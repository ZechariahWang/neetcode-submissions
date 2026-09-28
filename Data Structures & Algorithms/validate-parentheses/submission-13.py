class Solution:
    def isValid(self, s: str) -> bool:
        # approach: use a stack
        # we have a reference of close to open keys
        # loop through every character in the string
        # everytime we see a character thats NOT a closing bracket, append that to the stack bc its an opening character
        # if if the character is in close to open keys, then check if the stack is in that key vlaue maps to the actual value in the top of the stack
        # if it is, then so far its valid
        # otherwise, return false because this string is definitely not valid
        # outside, return true if the stack == [] bc we went through the entire string and it was valid 

        stack = []
        reference = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in reference.keys():
                if stack and stack[-1] == reference[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if stack ==[] else False

