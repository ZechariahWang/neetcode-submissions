class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = stones
        array.sort()
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
            
            array.sort()

        if len(array) == 0:
            array[0] = 0

        return array[0]




        
        