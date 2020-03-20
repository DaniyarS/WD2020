import math

a = int(input())
b = int(input())

for x in range(a, b):
    if math.sqrt(int(x))%2 == 0:
        print(str(x))