class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
# i는 최고 길이 회문의 첫 단 인덴스, l은 최고 길이 회문의 길이 j는 탐색 용
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]

