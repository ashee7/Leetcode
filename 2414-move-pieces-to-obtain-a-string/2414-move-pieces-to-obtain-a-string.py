class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startq=[]
        starts=[]
        targetq=[]
        targets=[]
        for i in range(len(start)):
            if start[i]!='_':
                startq.append((start[i],i))
                starts.append(start[i])
            if target[i]!='_':
                targetq.append((target[i],i))
                targets.append(target[i])

        if len(startq)!=len(targetq) or targets!=starts:
            return False
        
        for i in range(len(targetq)):
            if targetq[i][0]=='L' and startq[i][1]<targetq[i][1]:
                return False
            elif targetq[i][0]=='R' and startq[i][1]>targetq[i][1]:
                return False
            

        return True

        
