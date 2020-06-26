class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN=-(2**31)
        INT_MAX=2**31-1
        s=s.lstrip()
        asci=list(range(48,58))
        ans=[]
        p_m=[43,45]
        
        if len(s)==0:
            return 0
        
        if ord(s[0]) in p_m:
            ans.append(s[0])
            s=s[1:]

        if len(s)==0:
            return 0

        if ord(s[0]) not in asci:
            return 0

        for i in s:
            if ord(i) in asci:
                ans.append(i)
            else:
                break

        ans=''.join(ans)
        ans=int(float(ans))
        
        if ans<=INT_MAX and ans>=INT_MIN:
            return ans
        else:
            return [INT_MAX,INT_MIN][ans < 0]
        return ans