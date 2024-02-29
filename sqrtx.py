class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
           return 0
        g = x/2
        while True:
            new_g = (g + x/g)/2
            if abs(new_g - g) < 1e-9:
                return int(g)
            else:
                g = new_g