n = int(input())
mass = list(map(int, input().split()))
for i in range(0, n-1):
    elem = mass[i]
    index = i
    if elem % 2 == 0:
        print(mass[index], end = ' ')