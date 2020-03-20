a = int(input())
b = 0

for x in range(1 , a):
    if a%int(x) == 0:
        b+=1
print(b)