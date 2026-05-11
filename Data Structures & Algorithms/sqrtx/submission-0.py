class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        #handles the 0 and 1
        for i in range(x+1):
            sroot =  i * i
            if sroot == x:
                return i
            if sroot > x:
                return i-1