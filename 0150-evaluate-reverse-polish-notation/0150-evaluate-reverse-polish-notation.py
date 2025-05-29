class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=list()
        operators=set('+ - * /'.split())
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                num2=int(stack.pop())
                num1=int(stack.pop())
                if token=='+':
                    res=num1+num2
                elif token=='-':
                    res=num1-num2
                elif token == '*':
                    res=num1*num2
                elif token=='/':
                    res=num1/num2
                    if res<0:
                        res=ceil(res)
                    else:
                        res=floor(res)
                stack.append(res)        
        return int(stack.pop())