class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        for i in range(len(str1)):
            print(j)
            if str2[j]==str1[i] or (str1[i] == 'z' and str2[j]=='a') or str2[j]==chr(ord(str1[i])+1):
                # print(str2[j]==str1[i])
                # print(str2[j] == 'z' and str1[i]=='a')
                # print()
                j+=1
            if j==len(str2):
                return True
        return False