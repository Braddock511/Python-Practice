def valid_parentheses(string):
    y=[s for s in string]
    r=[]
    for x in y:
        if x=='(':
            r.append(x)
        if x==')':
            r.append(x)
    
    if  len(r)==0:
        return True
    else:
        open=0
        close=0
        for x in r:
            if x=='(':
                open+=1
            if x==')':
                close+=1
            if close>open:
                return False
                break
                
        if "".join(r).count('(')!="".join(r).count(')'):
            return False
        elif r[0]=='(' and r[-1]==')':
            return True
        else:
            return False

def test(fun, x):
    return fun == x

print(test(valid_parentheses("  ("), False))
print(test(valid_parentheses(")test"),False))
print(test(valid_parentheses(""),True))
print(test(valid_parentheses("hi())("),False))
print(test(valid_parentheses("hi(hi)()"),True))