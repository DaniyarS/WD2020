n = int(input())

sum = 0

mass = list(map(int, input().split()))
for i in range(0, n-1):
    elem = mass[i]
    index = i
    if elem > mass[index-1] and elem > mass[index+1]:
        sum += 1

print(sum)