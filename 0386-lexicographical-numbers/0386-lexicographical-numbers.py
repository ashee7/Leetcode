class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result=[]

        def findNextLexical(parent,limit,result):
            if parent>limit:
                return

            result.append(parent)

            for i in range(0,10):
                child=int(str(parent)+str(i))

                if child<=limit:
                    findNextLexical(child,limit,result)
                else:
                    break

        for i in range(1,10):
            if i<=n:
                findNextLexical(i,n,result)
            else: 
                break
        return result