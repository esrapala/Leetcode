
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        l=digits[:]
        if l[-1]!=9:
            l[-1]+=1
            return l
        n=0
        a=0
        for i in range(len(l)-1,-1,-1):
            n=n+(l[i]*(10**a))
            a+=1
        n+=1
        a=[]
        while n!=0:
            a.append(n%10)
            n//=10
        
        return a[::-1]

        