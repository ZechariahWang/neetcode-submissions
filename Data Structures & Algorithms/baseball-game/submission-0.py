class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            score = 0
            if operations[i].isdigit():
                score = int(operations[i])
                stack.append(score)
            elif operations[i] == "+":
                score = sum(stack)
                stack.append(score)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                score = stack[-1] * 2
                stack.append(score)

        return sum(stack)


        