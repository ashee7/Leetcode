class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x:int)->bool:
            num=list()
            while x:
                num.append(x%k)
                x//=k
            return num==num[::-1]
        
        cnt=0
        left=1
        total=0
        while cnt<n:
            right=left*10
            for op in range(2):
                for i in range(left,right):
                    if cnt==n:
                        break

                    x=i//10 if op==0 else i
                    combined=i
                    while x:
                        combined=x%10+combined*10
                        x//=10
                    if isPalindrome(combined):
                        cnt+=1
                        total+=combined
            left=right

        return total