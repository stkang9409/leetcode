class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        
        will_replace=['CM','CD','XC','XL','IX','IV']
        replace_to=['C'*9,'C'*4,'X'*9,'X'*4,'I'*9,'I'*4]
        ans=0
        n=0
        
        for i in range(len(will_replace)):
            s=s.replace(will_replace[i],replace_to[i])
            
        for c in s:
            ans+=roman[c]
                
        return ans