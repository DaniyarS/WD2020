a = int(input())
b = int(input())
c = int(input())
d = int(input())

def minimum(a, b, c, d):
    if a < b and a < c and a < d:
        print(a)
    elif b < a and b < c and b < d:
        print(b)
    elif c < a and c < b and c < d:
        print(c)
    else:
        print(d)

minimum(a, b, c, d)