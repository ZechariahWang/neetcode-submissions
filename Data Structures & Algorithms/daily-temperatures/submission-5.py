class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # plan:
        # answer array
        # stack stores (temp, index)
        # Loop through temperatures
        # while the stack isnt empty and current temp is warmer than top of stack
        # pop the element and compute days passed
        # push value into answer array, and also the current day into stacl
        # return answer

        answers = [0] * len(temperatures)
        stack = [] # (t, i)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                answers[stack_i] = i - stack_i
            stack.append((temperatures[i], i))
                
        return answers

        