class Solution:
    def maxDiff(self, num: int) -> int:
        maxi,mini=num,num
        notreplace1=False
        for dig in str(num):
            if dig!='9':
                maxi=str(num).replace(dig,'9')
                break

        for i,dig in enumerate(str(num)):
            if i==0:
                if dig=='1':
                    notreplace1=True
                    continue
                else:
                    mini=str(num).replace(dig,'1')
                    break
            elif dig!='0':
                if notreplace1 and dig=='1':
                    continue
                mini=str(num).replace(dig,'0')
                break

        print(mini,maxi)
        return int(maxi)-int(mini)