class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        lensearchword=len(searchWord)
        for i,word in enumerate(words):
            if word[:lensearchword]==searchWord:
                return i+1

        return -1