class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            score = 0
            if operations[i] == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                score = stack[-1] * 2
                stack.append(score)
            else:
                stack.append(int(operations[i]))

        return sum(stack)


        