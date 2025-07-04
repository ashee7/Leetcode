class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # def operation0(word):
        #     return word+word

        # def operation1(word):
        #     appending=''
        #     for char in word:
        #         nxt=chr(ord(char)+1) if ord(char)-ord('a')<26 else 'a'
        #         appending+=nxt

        #     return word+appending

        # result='a'
        # for operation in operations:
        #     if operation==0:
        #         result=operation0(result)
        #     else:
        #         result=operation1(result)
            
        # return result[k-1]
        
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))