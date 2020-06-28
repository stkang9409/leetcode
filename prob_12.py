class Solution:
    def intToRoman(self, num: int) -> str:
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman_div=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        n=0
        for i in roman_div:
            roman[n]=roman[n]*(num//i)
            n+=1
            num=num%i
        
        return "".join(roman)
        