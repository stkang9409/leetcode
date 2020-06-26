class Solution:
    def reverse(self, x: int) -> int:
        ans=str(abs(x))
        sign = [1,-1][x < 0]
        ans_int=sign*int(ans[::-1])
        if ans_int>=-2**31 and ans_int<=2**31-1:
            return ans_int
        return 0
