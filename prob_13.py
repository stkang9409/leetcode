class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) is 0:
            return ''''''
        
        strs.sort(key=len)
        first_word=strs[0]
        del strs[0]
        
        word=''
        longest_word=''
        test=True
        
        
        if '''''' in strs:
            return ''''''
        
        for i in range(len(first_word)):
            word=word+first_word[i]
            for s in strs:
                test*=(first_word[i]==s[i])
            
            if test:
                longest_word=word
            else:
                break
        
        return longest_word