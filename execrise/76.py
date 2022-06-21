a = list(input('傳送密碼(6位數整數)'))
b = ''
if len(a) < 6:
    print('Please enter more than 6 codes.')
elif len(a) > 6:
    print('Please enter less than 6 codes.')
else:
    for i in a:
        for j in range(10):
            if j*4%7 == int(i):
                b += str(j)
                break
    print('解密後的密碼:',b)
