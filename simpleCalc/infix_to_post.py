operatorlookup = set(('+', '-' , '*' , '/' , '^' ))
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
            while stack and stack[-1]!='(' and precedence[i] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(i)

        if i not in operatorlookup and i not in ('(',')') and i.isdigit()==False and i.isalpha()==False:
           postfix = f"'{i}' not suported yet"
           return postfix 

        
    while stack:
         postfix += stack.pop()

    return ' '.join(postfix)

# make test cases 
expressions = ['4*2+5*(2+1*3/4)/2', '4^2+5*(2+1)/2',  'A*(B+C)/D']
ans = ['4 2 * 5 2 1 3 * 4 / + * 2 / +',
    '4 2 ^ 5 2 1 + * 2 / +',
    'A B C + * D /']

for i in range(len(expressions)):
    res = infixToPostfix(expressions[i])
    print(res)

    



