ans = ['red','blue','red','green']
time = 0
while time <= 10:
    a = input('依序輸入四個顏色(中間以空白隔開)').split()
    if a == ans:
        print('You did it!')
        exit()
    else:
        if a[0] == 'red':
            c = 1
        elif a[0] == 'blue' or a[0] =='green':
            c = 2
        else:
            c = 3
        
        if a[1] == 'blue':
            c1 = 1
        elif a[1] == 'red' or a[1] =='green':
            c1 = 2
        else:
            c1 = 3
        
        if a[2] == 'red':
            c2 = 1
        elif a[2] == 'blue' or a[2] =='green':
            c2 = 2
        else:
            c2 = 3

        if a[3] == 'green':
            c3 = 1
        elif a[3] == 'red' or a[3] =='blue':
            c3 = 2
        else:
            c3 = 3
    print(c, c1, c2, c3)
    time += 1
print('Try again')