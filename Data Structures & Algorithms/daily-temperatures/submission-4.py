class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # plan:
        # one for loop iterate through temperatures i
        # one for loop iterate through temperatures j
        # compare if element at j < element at i:
        # if it is, increase consecutive days by 1
        # otherwise, append consecutive days to answers

        answers = [0] * len(temperatures)

        for i in range(len(temperatures)):
            consecutive_days=1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] <= temperatures[i]: # next day temp is lower, wont be valid so increase consectuvei days
                    consecutive_days += 1
                elif temperatures[j] > temperatures[i]: # if the temp is greater, its valid so append
                    answers[i] = consecutive_days
                    break

        return answers

        