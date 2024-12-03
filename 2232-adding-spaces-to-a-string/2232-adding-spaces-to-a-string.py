class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # counter=0
        # for space in spaces:
        #     s=s[:space+counter]+" "+s[space+counter:]
        #     counter+=1
        # return s
        res=""
        i=0
        for j in range(len(s)):
            if i<len(spaces) and spaces[i]==j:
                res+=" "
                i+=1
            res+=s[j]
        return res

