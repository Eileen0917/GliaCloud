def anonymous(x):
    return x**2 + 1

def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    temp = 0
    a=0
    b=0
    while intercept < end:
        intercept += step
        temp=step*anonymous(intercept)
        area+=temp
    return area

print(integrate(anonymous, 0, 10)) 