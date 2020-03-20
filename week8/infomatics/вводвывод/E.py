v = int(input())
t = int(input())

s = v*t

if v>0:
    while s > 109:
        s -= 109
    print(str(s))
else:
    while (-1)*s > 109:
        s -= 109
    print(str(int(109-((-1)*s))))