def EX3_1(n):
    x=0
    while True:
        if n==1:
            break
        elif n%2==0:
            n=n/2
            x=x+1
        elif n%2 > 0:
            n=n*3 + 1
            x=x+1
    return x
    
    
    
