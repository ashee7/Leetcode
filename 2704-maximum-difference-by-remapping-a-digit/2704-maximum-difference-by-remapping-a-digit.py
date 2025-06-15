class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_num,max_num=num,num
        for digit in str(num):
            if digit!='9':
                max_num=str(num).replace(digit,'9')
                break

        for digit in str(num):
            if digit!='0':
                min_num=str(num).replace(digit,'0')
                break
        
        return int(max_num)-int(min_num)