n = int(input())
mass = list(map(int, input().split()))

sum = 0

for i in range(0, n-1):
    elem = mass[i]
    index = i
    if elem > 0:
        sum += 1

print(sum)