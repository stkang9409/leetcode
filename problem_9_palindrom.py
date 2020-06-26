class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        n=0
        for i in range(int(len(s)/2)):
            if s[-(i+1)] == s[i]:
                continue
            else:
                return False
        return True
