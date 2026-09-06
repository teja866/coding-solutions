class Solution:
    def myPow(self, x: float, n: int) -> float:
        num=1
        if n<0:
            x=1/x
            n=-n
        while n>0:
            #id n is odd, multiply once
            if n%2==1:
                num*=x
            #square the base
            x*=x
            #halve the exponent
            n//=2
        return num