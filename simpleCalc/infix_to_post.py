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
        if i not in operatorlookup and i!= '(' and i!=')':
            postfix+=i

        if  i == '(':
            stack.append(i)

        if i == ')':
            while stack and stack[-1]!='(':
                p = stack.pop()
                postfix += p
            # discards the last '('
        if i == '(':
            stack.pop()

        if i in operatorlookup:
            if  not stack or stack[-1]=='(':
                stack.append(i)
            else:
                while stack and stack[-1]!='(' and precedence[i] <= precedence[stack[-1]]:
                    p = stack.pop()
                    postfix += p
                
                stack.append(i)

    while stack:
         p = stack.pop()
         postfix += p

    return postfix.replace(' ','')

# s = "((a+b)-c)*d)"
s = "(K + L - M*N + (O^P) * W/U/V * T + Q)"
ans = 'KL+MN*-OP^W*U/V/T*+Q+'
res = infixToPostfix(s)
print(res)
    



