import re 

operatorlookup = set(('+', '-' , '*' , '/' , '^' ))
precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}

def infixToPostfix(exp):
    ''' Given an infix expression returns a postfix expression '''
    postfix = []
    stack = []
    # whitout this 500 will be seen as 5 0 0 so wrong asnwers were giving 
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", exp)
    for i in tokens:
        # if an operand
        if i.isalnum():
            postfix.append(i)

        elif  i == '(':
            stack.append(i)

        elif i == ')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()

        if i in operatorlookup:
            while stack and stack[-1]!='(' and (precedence[i] <= precedence[stack[-1]]):
                postfix.append(stack.pop())
            stack.append(i)

        if i not in operatorlookup and i not in ('(',')') and i.isdigit()==False and i.isalpha()==False:
           postfix = f"'{i}' not suported yet"
           return postfix 
        
    while stack:
         postfix.append(stack.pop())

    return " ".join(postfix)
   


def eval_postfix(expression):
    stack = []
    exp = infixToPostfix(expression)
    tokens = exp.split()
    print(tokens)
    for i in tokens:
        if i.isdigit():
            stack.append(i)  
        else:
            a = stack.pop()
            b = stack.pop()
         
            if i=='+':
                res=int(b)+int(a) # old val <operator> recent value
            elif i=='-':
                res=int(b)-int(a)    
            elif i=='*':
                res=int(b)*int(a)
            elif i=='%':
                res=int(b)%int(a) 
            elif i=='/':
                res=int(b)/int(a)
            elif i=='^':
                res=int(b)**int(a)
    
            stack.append(res) # fina

    return ''.join(map(str,stack))
                  
  
# make test cases 
# expressions = ['4*2+5*(2+1*3/4)/2', '4^2+5*(2+1)/2',  'A*(B+C)/D']
# ans = ['4 2 * 5 2 1 3 * 4 / + * 2 / +',
#     '4 2 ^ 5 2 1 + * 2 / +',
#     'A B C + * D /']

# for i in range(len(expressions)):
#     res = eval_postfix(expressions[i])
#     print(res)

s = "(10*5)-500"
print(eval_postfix(s))
    



