n = int(input())

sum = 1

mass = list(map(int, input().split()))
for i in range(0, n-1):
    elem = mass[i]
    index = i
    if elem > mass[index-1]:
        sum +=1

print(sum)