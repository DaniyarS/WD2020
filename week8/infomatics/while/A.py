a = int(input())
x = 1

while x < a:
    x*=x
    if x < a:
        print(x)
        x+=1
    
