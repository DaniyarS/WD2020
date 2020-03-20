n = int(input())

sign = True

mass = list(map(int, input().split()))
if(sign == True):
    for i in range(0, n-1):
        elem = mass[i]
        index = i
        if (elem > 0) and (mass[index+1]>0):
            print('YES')
        elif elem < 0 and mass[index+1] < 0:
            print('YES')
        else:
            sign = False
else:
    print('NO')

