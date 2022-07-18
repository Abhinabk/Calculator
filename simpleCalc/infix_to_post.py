import operator 
operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}
precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
def infixToPostfix(exp):
    ''' Given an infix expression returns a postfix expression '''
    postfix = ""
    stack = []

    for i in exp:
        # if an operand
        if i.isalnum():
            postfix+=i

        elif  i == '(':
            stack.append(i)

        elif i == ')':
            top = stack.pop()
            while stack and top!='(':
                postfix += top
                top = stack.pop()

        if i in operatorlookup:
            if  not stack or stack[-1]=='(':
                stack.append(i)
            else:
                while stack and stack[-1]!='(' and precedence[i] <= precedence[stack[-1]]:
                    postfix += stack.pop()

                stack.append(i)

    while stack:
         postfix += stack.pop()

    return ' '.join(postfix)

expressions = ['4*2+5*(2+1)/2', '4^2+5*(2+1)/2',  'A*(B+C)/D']
for s in expressions:
    res = infixToPostfix(s)
    print(res)
    



