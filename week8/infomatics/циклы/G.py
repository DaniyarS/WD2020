a = int(input())

for x in range(2, a):
    if a%int(x) == 0:
        print(str(x))
        break