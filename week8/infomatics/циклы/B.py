a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(c, d):
    mod = int(c%d)
    for x in range(a, b):
        index = int(x)
        if mod == index:
            print(mod + '\n')
