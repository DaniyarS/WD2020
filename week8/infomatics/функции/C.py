a = int(input())
b = int(input())

def xor(x , y):
    return bool(x) ^ bool(y)

print(xor(a, b))