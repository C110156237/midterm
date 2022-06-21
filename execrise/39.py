num = int(input("請輸入一整數"))
for i in range (num):
    for a in range(num-i):
        print(' ',end='')
    for a in range(2*i+1):
        if a%2==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()
for i in range (num-1,1,-1):
    for a in range(num-i):
        print(' ',end='')
    for a in range(2*i-1):
        if a%2==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()

