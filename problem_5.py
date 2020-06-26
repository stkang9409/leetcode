class Solution:
    def convert(self, s: str, numRows: int) -> str:
        create_position=[]
        ans=''
        switch=-1
        n=0
        
        if numRows<=1:
            return s
        
        for i in range(len(s)):
            create_position.append([n,s[i]])
            if n==numRows-1 or n==0:
                switch*=-1
            n+=switch
        check=0
        while check<numRows:
            for n in create_position:
                if check in n:
                    ans+=n[1]
            check+=1
        return ans

"""
Other person Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ['' for _ in range(numRows)]  (이게 핵심이네, 변수만큼 개수의 원소를 지닌 리스트 정의)
        flag = -1
        idx = 0
        for c in s:
            res[idx] += c
            if idx in [0, numRows-1]:
                flag = -flag
            idx += flag
        return ''.join(res) 
"""
