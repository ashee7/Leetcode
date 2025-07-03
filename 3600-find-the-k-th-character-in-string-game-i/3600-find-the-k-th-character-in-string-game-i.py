class Solution:
    

    def kthCharacter(self, k: int) -> str:

        def operate(word):
            appending=''
            for i in range(len(word)):
                appending+=chr(ord(word[i])+1) 

            return word+appending

        word='a'
        while len(word)<k:
            word=operate(word)
        return word[k-1]
