class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = stones
        array.sort()
        res=0
        while len(array) > 1:
            x = array[-2]
            y = array[-1]

            if x < y:
                res = y - x
                array.remove(x)
                array.remove(y)
                array.append(res)
            elif x > y:
                res = x - y
                array.remove(x)
                array.remove(y)
                array.append(res)
            else:
                res = 1
                array.remove(x)
                array.remove(y)
                array.append(res)

        return res




        
        