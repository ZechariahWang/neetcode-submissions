class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                result=(int(stack.pop())+int(stack.pop()))
                stack.append(result)
            elif tokens[i]=="-":
                result=(int(stack.pop())-int(stack.pop()))
                stack.append(result)
            elif tokens[i]=="*":
                result=(int(stack.pop())*int(stack.pop()))
                stack.append(result)
            elif tokens[i]=="/":
                a,b=stack.pop(),stack.pop()
                result=(int(a/b))
                stack.append(result)
            else:
                stack.append(tokens[i])

        return int(stack[-1])